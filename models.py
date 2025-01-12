from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BackupJob(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    source_path = db.Column(db.String(200), nullable=False)
    destination = db.Column(db.String(200), nullable=False)
    schedule = db.Column(db.String(50), nullable=True)  # e.g., "daily", "weekly"
    created_at = db.Column(db.DateTime, default=db.func.now())

