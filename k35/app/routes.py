from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.models import User, Story, Edit
from app.forms import LoginForm, RegistrationForm, EditForm
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/home')
def home():
    stories = Story.query.all()
    return render_template('home.html', title='Home', stories=stories)

@app.route('/in_progress')
def in_progress():
    stories = Story.query.filter_by(completed=False).all()
    return render_template('in_progress.html', title='Stories In Progress', stories=stories)

@app.route('/completed')
def completed():
    stories = Story.query.filter_by(completed=True).all()
    return render_template('completed.html', title='Completed Stories', stories=stories)

@app.route('/contributions')
@login_required
def contributions():
    user_edits = Edit.query.filter_by(user_id=current_user.id).all()
    return render_template('contributions.html', title='Your Contributions', edits=user_edits)

@app.route('/story/<int:story_id>', methods=['GET', 'POST'])
@login_required
def story(story_id):
    story = Story.query.get_or_404(story_id)
    last_edit = story.edits.order_by(Edit.timestamp.desc()).first()
    form = EditForm()
    if form.validate_on_submit():
        edit = Edit(body=form.body.data, author=current_user, story=story)
        db.session.add(edit)
        db.session.commit()
        flash('Your edit has been added.')
        return redirect(url_for('story', story_id=story.id))
    return render_template('story_edit.html', title='Edit Story', form=form, last_edit=last_edit)