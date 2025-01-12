from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    # Create the Flask app instance
    app = Flask(__name__)

    # Application configuration
    app.config.from_mapping(
        SECRET_KEY='PASS',  # Replace with a secure random key
        SQLALCHEMY_DATABASE_URI='sqlite:///backup.db',  # SQLite database file
        SQLALCHEMY_TRACK_MODIFICATIONS=False,  # Disable event notifications for performance
        B2_BUCKET_NAME='your-bucket-name',
        B2_ACCESS_KEY_ID='your-access-key-id',
        B2_SECRET_ACCESS_KEY='your-secret-access-key',
        B2_ENDPOINT_URL='https://s3.us-west-002.backblazeb2.com'  # Example endpoint
    )

    # Initialize the database with the app
    db.init_app(app)

    # Import and register the main blueprint
    from app.routes import main
    app.register_blueprint(main)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app

