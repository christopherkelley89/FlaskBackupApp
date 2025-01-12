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
- Clone the repository and navigate to the project directory.
### Create a virtual environment
#### Linux
```
bash
python -m venv venv
 source venv/bin/activate 
```
#### For Windows 
```
venv\Scripts\activate
```
## Install dependencies
```
bash
pip install -r requirements.txt
```
## Set up your Backblaze B2 credentials in app/__init__.py
python
```
app.config.from_mapping(
    B2_BUCKET_NAME='your-bucket-name',
    B2_ACCESS_KEY_ID='your-access-key-id',
    B2_SECRET_ACCESS_KEY='your-secret-access-key',
    B2_ENDPOINT_URL='your-endpoint-url'
)
```
## Initialize the database
```
bash
python run.py
```
## Start the application
```
bash
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
```
## Deployment
- This application can be deployed using any WSGI-compatible server. For example, you can use Gunicorn:
```
bash
gunicorn -w 4 run:app
```

## Dependencies 
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- boto3
# Docker
- Testing using Docker Compose 
- Create the Docker Compose File Ensure the compose.yml file is present in the root of the project. Here's a sample structure:

## yaml
```
version: "3.8"

services:
  flask-app:
    image: flask-app:latest
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "5000:5000"
    environment:
      FLASK_ENV: production
      B2_BUCKET_NAME: your-bucket-name
      B2_ACCESS_KEY_ID: your-access-key-id
      B2_SECRET_ACCESS_KEY: your-secret-access-key
      B2_ENDPOINT_URL: https://s3.us-west-002.backblazeb2.com
    volumes:
      - ./data:/app/data
    restart: unless-stopped

volumes:
  data:
    driver: local
```
- Create the Dockerfile Ensure the Dockerfile is present in the project root. Example:

## dockerfile
```
FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "run.py"]
```
- Build and Run the Containers Run the following command to build the Docker image and start the containers:

```
bash
docker-compose up --build
```
- Access the Flask App Once the container is running, open your browser and navigate to:
http://localhost:5000

## Environment Variables 
- Replace the placeholder values in the docker-compose.yml file under the environment section with your actual Backblaze B2 bucket credentials.
- Persistent Data The SQLite database and other data are stored in the data folder. This folder is mapped as a volume to persist data even when the container is restarted.


