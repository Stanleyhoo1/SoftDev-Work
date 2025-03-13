import sqlite3
from flask import Flask, g, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['DATABASE'] = 'stories.db'

login_manager = LoginManager(app)
login_manager.login_view = 'home'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    db.commit()

# Ensure tables are initialized on every request.
@app.before_request
def ensure_tables():
    init_db()

# User class compatible with Flask-Login.
class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def get(user_id):
        db = get_db()
        user = db.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        if user is None:
            return None
        return User(user['id'], user['username'], user['password'])

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# Helper to check if a user has contributed to a story.
def has_contributed(story_id, user_id):
    if not user_id:
        return False
    db = get_db()
    edit = db.execute("SELECT * FROM edits WHERE story_id = ? AND user_id = ?", (story_id, user_id)).fetchone()
    return edit is not None

# Inject helper into all templates.
@app.context_processor
def inject_helpers():
    return dict(has_contributed=lambda story, user: has_contributed(story['id'], user.id) if user and user.is_authenticated else False)

# ----------------------
# Authentication Routes
# ----------------------
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    db = get_db()
    user = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    if user and user['password'] == password:
        user_instance = User(user['id'], user['username'], user['password'])
        login_user(user_instance)
        flash("Logged in successfully!", "success")
    else:
        flash("Invalid credentials", "error")
    return redirect(request.referrer or url_for('home'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully!", "success")
    return redirect(request.referrer or url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    db = get_db()
    if request.method == 'POST':
        username = request.form.get('reg_username')
        password = request.form.get('reg_password')
        existing = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        if existing:
            flash("Username already exists.", "error")
            return redirect(request.referrer or url_for('register'))
        db.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        db.commit()
        flash("Registered successfully. Please log in.", "success")
        return redirect(url_for('home'))
    return render_template('register.html')

# ----------------------
# Story Routes
# ----------------------
@app.route('/')
def home():
    db = get_db()
    stories = db.execute("SELECT * FROM stories").fetchall()
    stories_with_edit = []
    for story in stories:
        last_edit = db.execute("SELECT * FROM edits WHERE story_id = ? ORDER BY timestamp DESC", (story['id'],)).fetchone()
        story_dict = dict(story)
        story_dict['last_edit'] = last_edit
        stories_with_edit.append(story_dict)
    return render_template('home.html', stories=stories_with_edit)

@app.route('/create_story', methods=['GET', 'POST'])
@login_required
def create_story():
    db = get_db()
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        if not title or not content:
            flash("Both title and content are required.", "error")
            return redirect(url_for('create_story'))
        # Check for duplicate title
        existing_story = db.execute("SELECT * FROM stories WHERE title = ?", (title,)).fetchone()
        if existing_story:
            flash("A story with that title already exists. Please choose a different title.", "error")
            return redirect(url_for('create_story'))
        # Insert story with creator_id as current user's id.
        db.execute("INSERT INTO stories (title, status, creator_id) VALUES (?, ?, ?)", (title, "in_progress", current_user.id))
        db.commit()
        story_id = db.execute("SELECT last_insert_rowid()").fetchone()[0]
        timestamp = datetime.now().isoformat(' ', 'seconds')
        db.execute("INSERT INTO edits (content, story_id, user_id, timestamp) VALUES (?, ?, ?, ?)",
                   (content, story_id, current_user.id, timestamp))
        db.commit()
        flash("Story created successfully!", "success")
        return redirect(url_for('home'))
    return render_template('create_story.html')

@app.route('/story/<int:story_id>')
def story_detail(story_id):
    db = get_db()
    story = db.execute("SELECT * FROM stories WHERE id = ?", (story_id,)).fetchone()
    last_edit = db.execute("SELECT * FROM edits WHERE story_id = ? ORDER BY timestamp DESC", (story_id,)).fetchone()
    display_content = last_edit['content'] if last_edit else ""
    return render_template('story_detail.html', story=story, last_edit=last_edit, display_content=display_content)

@app.route('/story/<int:story_id>/history')
def edit_history(story_id):
    db = get_db()
    story = db.execute("SELECT * FROM stories WHERE id = ?", (story_id,)).fetchone()
    if not (story['status'] == 'completed' or has_contributed(story['id'], current_user.id if current_user.is_authenticated else None)):
        flash("You are not allowed to view the full edit history.", "error")
        return redirect(url_for('story_detail', story_id=story_id))
    edits = db.execute("SELECT * FROM edits WHERE story_id = ? ORDER BY timestamp", (story_id,)).fetchall()
    return render_template('edit_history.html', story=story, edits=edits)

@app.route('/completed_story/<int:story_id>')
def completed_story_view(story_id):
    db = get_db()
    story = db.execute("SELECT * FROM stories WHERE id = ?", (story_id,)).fetchone()
    if story['status'] != 'completed':
        flash("Story is not completed.", "error")
        return redirect(url_for('story_detail', story_id=story_id))
    edits = db.execute("SELECT * FROM edits WHERE story_id = ? ORDER BY timestamp", (story_id,)).fetchall()
    full_text = "\n\n".join([edit['content'] for edit in edits])
    contributors_rows = db.execute(
        "SELECT DISTINCT u.username FROM users u JOIN edits e ON u.id = e.user_id WHERE e.story_id = ?",
        (story_id,)
    ).fetchall()
    contributors = ", ".join([row['username'] for row in contributors_rows])
    return render_template('completed_story_view.html', story=story, full_text=full_text, contributors=contributors)

@app.route('/contribute/<int:story_id>', methods=['GET', 'POST'])
@login_required
def contribute_story(story_id):
    db = get_db()
    story = db.execute("SELECT * FROM stories WHERE id = ?", (story_id,)).fetchone()
    if has_contributed(story['id'], current_user.id):
        flash("You have already contributed.", "error")
        return redirect(url_for('story_detail', story_id=story_id))
    last_edit = db.execute("SELECT * FROM edits WHERE story_id = ? ORDER BY timestamp DESC", (story_id,)).fetchone()
    if request.method == 'POST':
        new_content = request.form.get('new_content')
        complete_story = request.form.get('complete_story')
        if not new_content:
            flash("Contribution content required.", "error")
            return redirect(url_for('contribute_story', story_id=story_id))
        timestamp = datetime.now().isoformat(' ', 'seconds')
        db.execute("INSERT INTO edits (content, story_id, user_id, timestamp) VALUES (?, ?, ?, ?)",
                   (new_content, story_id, current_user.id, timestamp))
        if complete_story == 'on':
            db.execute("UPDATE stories SET status = 'completed' WHERE id = ?", (story_id,))
        db.commit()
        flash("Contribution submitted.", "success")
        return redirect(url_for('home'))
    return render_template('contribute_story.html', story=story, last_edit=last_edit)

# New route for editing the story title (only the creator can do this)
@app.route('/edit_story_title/<int:story_id>', methods=['GET', 'POST'])
@login_required
def edit_story_title(story_id):
    db = get_db()
    story = db.execute("SELECT * FROM stories WHERE id = ?", (story_id,)).fetchone()
    if story is None:
        flash("Story not found.", "error")
        return redirect(url_for('home'))
    # Only allow the creator to edit the title
    if int(story['creator_id']) != int(current_user.id):
        flash("You are not authorized to edit this story's title.", "error")
        return redirect(url_for('story_detail', story_id=story_id))
    if request.method == 'POST':
        new_title = request.form.get('new_title')
        if not new_title:
            flash("Title cannot be empty.", "error")
            return redirect(url_for('edit_story_title', story_id=story_id))
        # Check if the new title is unique (or same as current title)
        existing_story = db.execute("SELECT * FROM stories WHERE title = ? AND id != ?", (new_title, story_id)).fetchone()
        if existing_story:
            flash("A story with that title already exists. Please choose a different title.", "error")
            return redirect(url_for('edit_story_title', story_id=story_id))
        db.execute("UPDATE stories SET title = ? WHERE id = ?", (new_title, story_id))
        db.commit()
        flash("Story title updated successfully!", "success")
        return redirect(url_for('story_detail', story_id=story_id))
    return render_template('edit_story_title.html', story=story)

@app.route('/in_progress')
def in_progress():
    db = get_db()
    stories = db.execute("SELECT * FROM stories WHERE status != 'completed'").fetchall()
    stories_with_edit = []
    for story in stories:
        last_edit = db.execute("SELECT * FROM edits WHERE story_id = ? ORDER BY timestamp DESC", (story['id'],)).fetchone()
        story_dict = dict(story)
        story_dict['last_edit'] = last_edit
        stories_with_edit.append(story_dict)
    return render_template('in_progress.html', stories=stories_with_edit)

@app.route('/completed')
def completed():
    db = get_db()
    stories = db.execute("SELECT * FROM stories WHERE status = 'completed'").fetchall()
    stories_with_edit = []
    for story in stories:
        last_edit = db.execute("SELECT * FROM edits WHERE story_id = ? ORDER BY timestamp DESC", (story['id'],)).fetchone()
        story_dict = dict(story)
        story_dict['last_edit'] = last_edit
        stories_with_edit.append(story_dict)
    return render_template('completed_stories.html', stories=stories_with_edit)

@app.route('/contributions')
@login_required
def contributions():
    db = get_db()
    contributed_edits = db.execute("SELECT * FROM edits WHERE user_id = ?", (current_user.id,)).fetchall()
    story_ids = {edit['story_id'] for edit in contributed_edits}
    placeholders = ",".join("?" for _ in story_ids)
    query = f"SELECT * FROM stories WHERE id IN ({placeholders})" if story_ids else "SELECT * FROM stories WHERE 1=0"
    stories = db.execute(query, tuple(story_ids)).fetchall() if story_ids else []
    stories_with_edit = []
    for story in stories:
        last_edit = db.execute("SELECT * FROM edits WHERE story_id = ? ORDER BY timestamp DESC", (story['id'],)).fetchone()
        story_dict = dict(story)
        story_dict['last_edit'] = last_edit
        stories_with_edit.append(story_dict)
    return render_template('contributions.html', stories=stories_with_edit)

if __name__ == '__main__':
    app.run(debug=True)