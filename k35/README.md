# Story Blog Website

This is a Flask application for a story blog website where users can write and share their stories.

## Features

- User registration and authentication
- CRUD operations for stories
- Commenting on stories
- User profiles

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/story-blog.git
    cd story-blog
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. Run the application:
    ```bash
    flask run
    ```

## Project Structure

```
story-blog/
    ├── app/
    │   ├── __init__.py
    │   ├── models.py
    │   ├── routes.py
    │   ├── static/
    │   ├── templates/
    │   └── forms.py
    ├── migrations/
    ├── venv/
    ├── .env
    ├── config.py
    ├── requirements.txt
    ├── run.py
    └── README.md
```

## Deployment

Instructions for deploying the application will go here.

## License

This project is licensed under the MIT License.