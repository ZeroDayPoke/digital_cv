# Use Python 3.10 slim image as the base
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /

# Install system dependencies
RUN apt-get update && apt-get install -y libmariadb-dev-compat pkg-config build-essential && apt-get clean

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python packages listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn WSGI server
RUN python3.10 -m pip install gunicorn

# Copy the entire application from the host to the container's working directory
COPY . .

RUN pybabel compile -d translations

# Command to run when the container starts: Use Gunicorn to serve the Flask application using the configuration file
CMD ["gunicorn", "-c", "gunicorn_config.py", "wsgi:app"]
