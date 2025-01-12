
import boto3
from flask import current_app

def upload_to_b2(file_path, file_name):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=current_app.config['B2_ACCESS_KEY_ID'],
        aws_secret_access_key=current_app.config['B2_SECRET_ACCESS_KEY'],
        endpoint_url=current_app.config['B2_ENDPOINT_URL']
    )
    bucket_name = current_app.config['B2_BUCKET_NAME']
    s3_client.upload_file(file_path, bucket_name, file_name)