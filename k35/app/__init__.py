from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stories.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'home'

# Models
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='in_progress')  # 'in_progress' or 'completed'
    edits = db.relationship('Edit', backref='story', lazy=True)

class Edit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    story_id = db.Column(db.Integer, db.ForeignKey('story.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Helper function to check if a user has contributed to a story.
def has_contributed(story, user):
    if not user or not user.is_authenticated:
        return False
    return Edit.query.filter_by(story_id=story.id, user_id=user.id).first() is not None

# ----------------------
# Authentication Routes
# ----------------------
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        login_user(user)
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
    if request.method == 'POST':
        username = request.form.get('reg_username')
        password = request.form.get('reg_password')
        if User.query.filter_by(username=username).first():
            flash("Username already exists.", "error")
            return redirect(request.referrer or url_for('home'))
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registered successfully. Please log in.", "success")
        return redirect(url_for('home'))
    return render_template('register.html')

# ----------------------
# Story Routes
# ----------------------
@app.route('/')
def home():
    stories = Story.query.all()
    return render_template('home.html', stories=stories, has_contributed=has_contributed)

@app.route('/create_story', methods=['GET', 'POST'])
@login_required
def create_story():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        if not title or not content:
            flash("Both title and content are required.", "error")
            return redirect(url_for('create_story'))
        new_story = Story(title=title, status='in_progress')
        db.session.add(new_story)
        db.session.commit()
        new_edit = Edit(content=content, story_id=new_story.id, user_id=current_user.id, timestamp=db.func.now())
        db.session.add(new_edit)
        db.session.commit()
        flash("Story created successfully!", "success")
        return redirect(url_for('home'))
    return render_template('create_story.html')

@app.route('/story/<int:story_id>')
def story_detail(story_id):
    story = Story.query.get_or_404(story_id)
    last_edit = Edit.query.filter_by(story_id=story.id).order_by(Edit.timestamp.desc()).first()
    # Always display the full last edit when viewing an individual story.
    display_content = last_edit.content if last_edit else ""
    return render_template('story_detail.html', story=story, last_edit=last_edit, display_content=display_content, has_contributed=has_contributed)

@app.route('/story/<int:story_id>/history')
def edit_history(story_id):
    story = Story.query.get_or_404(story_id)
    if not (story.status == 'completed' or has_contributed(story, current_user)):
        flash("You are not allowed to view the full edit history.", "error")
        return redirect(url_for('story_detail', story_id=story_id))
    edits = Edit.query.filter_by(story_id=story.id).order_by(Edit.timestamp).all()
    return render_template('edit_history.html', story=story, edits=edits)

@app.route('/completed_story/<int:story_id>')
def completed_story_view(story_id):
    story = Story.query.get_or_404(story_id)
    if story.status != 'completed':
        flash("Story is not completed.", "error")
        return redirect(url_for('story_detail', story_id=story_id))
    edits = Edit.query.filter_by(story_id=story.id).order_by(Edit.timestamp).all()
    full_text = "\n\n".join([edit.content for edit in edits])
    # Get a distinct list of contributor usernames for this story.
    contributors_query = db.session.query(User.username).join(Edit).filter(Edit.story_id == story.id).distinct().all()
    contributors = ", ".join([row[0] for row in contributors_query])
    return render_template('completed_story_view.html', story=story, full_text=full_text, contributors=contributors)

@app.route('/contribute/<int:story_id>', methods=['GET', 'POST'])
@login_required
def contribute_story(story_id):
    story = Story.query.get_or_404(story_id)
    if has_contributed(story, current_user):
        flash("You have already contributed.", "error")
        return redirect(url_for('story_detail', story_id=story_id))
    last_edit = Edit.query.filter_by(story_id=story.id).order_by(Edit.timestamp.desc()).first()
    if request.method == 'POST':
        new_content = request.form.get('new_content')
        complete_story = request.form.get('complete_story')
        if not new_content:
            flash("Contribution content required.", "error")
            return redirect(url_for('contribute_story', story_id=story_id))
        new_edit = Edit(content=new_content, story_id=story.id, user_id=current_user.id, timestamp=db.func.now())
        db.session.add(new_edit)
        if complete_story == 'on':
            story.status = 'completed'
        db.session.commit()
        flash("Contribution submitted.", "success")
        return redirect(url_for('home'))
    return render_template('contribute_story.html', story=story, last_edit=last_edit)

@app.route('/in-progress')
def in_progress():
    stories = Story.query.filter(Story.status != 'completed').all()
    return render_template('stories_in_progress.html', stories=stories, has_contributed=has_contributed)

@app.route('/completed')
def completed():
    stories = Story.query.filter_by(status='completed').all()
    return render_template('completed_stories.html', stories=stories)

@app.route('/contributions')
@login_required
def contributions():
    contributed_edits = Edit.query.filter_by(user_id=current_user.id).all()
    story_ids = {edit.story_id for edit in contributed_edits}
    stories = Story.query.filter(Story.id.in_(story_ids)).all()
    return render_template('contributions.html', stories=stories)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)