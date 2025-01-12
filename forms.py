from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class BackupJobForm(FlaskForm):
    name = StringField('Job Name', validators=[DataRequired()])
    source_path = StringField('Source Path', validators=[DataRequired()])
    destination = StringField('Destination', validators=[DataRequired()])
    schedule = StringField('Schedule')
    submit = SubmitField('Add Backup Job')
