# Story Blog - StoryMagic

Welcome to **Story Blog - StoryMagic**, a magical storytelling platform where users collaboratively create, contribute to, and complete enchanting stories. Our platform features a unique, earthy design with decorative fonts, text shadows, and organic textures that evoke a timeless, mystical ambiance.

## Features

- **User Authentication**: 
  - Register, log in, and log out securely.
- **Unique Story Titles**:
  - Prevent duplicate titles to ensure every story stands out.
- **Collaborative Story Creation**:
  - Create new stories and contribute to existing ones.
- **Edit History**:
  - View full edits for each story, preserving all formatting (spaces, newlines, tabs).
- **Original Creator Controls**:
  - Only the story creator can update the story title via a dedicated interface.
- **Magical Themed UI**:
  - Enjoy a consistent, magical theme throughout the site with decorative fonts, earthy colors, and subtle text shadows.
- **Team Flag**:
  - Proudly display our custom team flag component representing *Team StoryMagic*.

## Technologies

- **Backend**: Python with Flask
- **Database**: SQLite (auto-initializes tables if they don't exist)
- **User Authentication**: Flask-Login
- **Frontend**: HTML, CSS, and Jinja2 templating with a cohesive magical design

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Stanleyhoo1/story-blog.git
   cd story-blog
   ```

2. **Create a Virtual Environment and Install Dependencies**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Run the Application**

   ```bash
   flask run
   ```

   The application uses `stories.db` as its SQLite database. On every request, the necessary database tables will be created if they do not already exist.

## Usage

1. **User Registration & Login**
   - Register a new account or log in with your credentials.
   
2. **Story Creation**
   - Click on **Create New Story**.
   - Enter a unique title and initial content to start your story.
   
3. **Contributing to Stories**
   - Browse stories on the homepage, in-progress, or contributions sections.
   - Click on **Contribute** for any story you haven’t contributed to yet.
   
4. **Viewing Stories**
   - Click on a story to view its content.
   - For completed stories, view the entire formatted content (with preserved spacing and newlines), edit history, and list of contributors.
   - If you are the story's original creator, an **Edit Title** button is provided for renaming the story.

5. **Team Flag Feature**
   - Our custom team flag is displayed on the site, symbolizing our commitment to creative collaboration and magical storytelling.

## File Structure

- `app/__init__.py`  
  The main Flask application file containing routes for authentication, story management, and database initialization.
  
- `app/templates/`  
  Contains all HTML/Jinja2 templates:
  - `base.html`: Main base template.
  - `home.html`, `in_progress.html`, `completed_stories.html`, etc.: Templates for different pages.
  - `story_detail.html`: Template for viewing a story with preserved formatting.
  - `edit_story_title.html`: Template for editing a story title (accessible only by the creator).
  - `teamflag.html`: Reusable component for displaying the team flag.
  
- `app/static/`  
  Houses static files:
  - `styles.css`: Magical, earthy-themed CSS styles.
  - `images/`: Directory containing images such as the team flag image (`teamflag.png`).
  
- `schema.sql`  
  SQL file defining the database schema for `users`, `stories`, and `edits` with appropriate constraints.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

Distributed under the MIT License. See the `LICENSE` file for more information.
