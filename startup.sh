#!/bin/bash

# Activate virtual environment (if applicable)
source venv/bin/activate  # Update path to your virtual environment

# Set the application environment (optional)
export FLASK_APP=app.py
export FLASK_ENV=production  # Use 'development' for debugging

# Run Gunicorn
gunicorn --workers 4 --bind 0.0.0.0:8000 app:app  # Replace 'app:app' with 'module_name:app_instance'
