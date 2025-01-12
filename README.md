# FlaskBackupApp

## Overview
- The Flask Backup Application is designed to manage and automate backup jobs. It features a simple web interface for creating and managing backup tasks, storing them in a database, and uploading files to Backblaze B2 cloud storage.

## Features
- Backup Management: Create, view, and delete backup jobs through a web interface.
- Cloud Integration: Upload files to a Backblaze B2 bucket using the Boto3 library.
- Database Support: Store backup job details in a SQLite database.
- Form Validation: Ensure required fields are filled using Flask-WTF.
- RESTful API Endpoints: Access and manage backup jobs programmatically.

## Project Structure
```
├── app/
│   ├── __init__.py        # App initialization and configuration
│   ├── models.py          # Database models
│   ├── routes.py          # Application routes and logic
│   ├── forms.py           # Flask-WTF forms for validation
│   ├── backup.py          # Backup and cloud upload logic
├── templates/
│   └── index.html         # Frontend interface
├── requirements.txt       # Project dependencies
├── run.py                 # Entry point for running the application
```
 
## Installation
### Prerequisites
Ensure you have Python 3.x installed. You will also need access to a Backblaze B2 bucket.

## Steps
Clone the repository and navigate to the project directory.
### Create a virtual environment
bash
python -m venv venv
### source venv/bin/activate 
### For Windows: venv\Scripts\activate

## Install dependencies
bash
pip install -r requirements.txt

## Set up your Backblaze B2 credentials in app/__init__.py:
python
```
app.config.from_mapping(
    B2_BUCKET_NAME='your-bucket-name',
    B2_ACCESS_KEY_ID='your-access-key-id',
    B2_SECRET_ACCESS_KEY='your-secret-access-key',
    B2_ENDPOINT_URL='your-endpoint-url'
)
```
## Initialize the database:
bash
python run.py
Usage
Start the application:
bash
Copy code
python run.py
Access the app in your browser at http://localhost:5000.
Use the form to add backup jobs, specifying:
Job Name
Source Path
Destination
Schedule (optional)
View or delete existing jobs using the REST API or the web interface.
API Endpoints
GET /backups - Retrieve all backup jobs.
POST /backup - Create a new backup job.
DELETE /backup/<id> - Delete a backup job by its ID.

## Deployment
- This application can be deployed using any WSGI-compatible server. For example, you can use Gunicorn:

bash
gunicorn -w 4 run:app
Dependencies
See requirements.txt:

## Dependencies 
Flask
Flask-SQLAlchemy
Flask-WTF
boto3
