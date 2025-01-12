from flask import Blueprint, render_template, request, jsonify
from .models import BackupJob
from . import db
from .backup import upload_to_b2
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/backup', methods=['POST'])
def backup():
    try:
        # Get data from the request
        data = request.form
        name = data.get('name')
        source = data.get('source')
        destination = data.get('destination')
        schedule = data.get('schedule', None)

        # Validate required fields
        if not name or not source or not destination:
            return jsonify({'error': 'Missing required fields'}), 400

        # Create a new BackupJob instance
        new_backup = BackupJob(
            name=name,
            source_path=source,
            destination=destination,
            schedule=schedule
        )

        # Add to the database
        db.session.add(new_backup)
        db.session.commit()

        # Perform the backup
        file_name = os.path.basename(source)
        upload_to_b2(source, file_name)

        return jsonify({'message': 'Backup job created and file uploaded successfully!'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main.route('/backups', methods=['GET'])
def get_backups():
    try:
        # Retrieve all backup jobs from the database
        backups = BackupJob.query.all()
        backups_list = [
            {
                'id': backup.id,
                'name': backup.name,
                'source': backup.source_path,
                'destination': backup.destination,
                'schedule': backup.schedule
            }
            for backup in backups
        ]
        return jsonify(backups_list), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main.route('/backup/<int:id>', methods=['DELETE'])
def delete_backup(id):
    try:
        # Find the backup job by ID
        backup = BackupJob.query.get(id)
        if not backup:
            return jsonify({'error': 'Backup job not found'}), 404

        # Delete the backup job
        db.session.delete(backup)
        db.session.commit()

        return jsonify({'message': 'Backup job deleted successfully!'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500