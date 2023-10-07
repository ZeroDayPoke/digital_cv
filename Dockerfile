# Use Ubuntu 22.04 (Jammy) as the base image for the container
FROM ubuntu:22.04

# Set environment variable to prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Define the working directory inside the container
WORKDIR /app

# Update package lists, add repository for newer Python versions, and install Python 3.10 along with essential tools
RUN apt-get update && apt-get install -y \
    software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get install -y python3.10 python3.10-venv python3.10-dev python3-pip \
    && python3.10 -m pip install --upgrade pip

# Copy the requirements file from the host to the container's working directory
COPY requirements.txt .

# Install Python packages listed in requirements.txt
RUN python3.10 -m pip install --no-cache-dir -r requirements.txt

# Install Gunicorn WSGI server
RUN python3.10 -m pip install gunicorn

# Copy the entire application from the host to the container's working directory
COPY . .

# Command to run when the container starts: Use Gunicorn to serve the Flask application using the configuration file
CMD ["gunicorn", "-c", "gunicorn_config.py", "wsgi:app"]
