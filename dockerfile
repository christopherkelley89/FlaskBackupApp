# Use an official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask app's default port
EXPOSE 5000

# Start the Flask app
CMD ["python", "run.py"]
