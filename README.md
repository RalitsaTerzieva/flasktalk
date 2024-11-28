# FlaskTalk Application

FlaskTalk is a dynamic web application built to practice creating and managing blog posts, leveraging Flask and various libraries. This project integrates Flask, SQLAlchemy, Flask-Migrate, WTForms, and SQLite to offer a platform for users to post, edit, and manage content.

---

## Installation

### Prerequisites
Ensure you have Python (3.7 or higher) and `pip` installed on your machine.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/RalitsaTerzieva/flasktalk
   cd pawadopt

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   
4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   
6. Initialize the database:
   ```bash
   export FLASK_APP=app.py
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   
8. Run the application:
   ```bash
   flask run
