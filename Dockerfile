# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file and install the dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Expose port 5000 to allow external access
EXPOSE 5000

# Define environment variable to tell Flask it is in development mode
ENV FLASK_ENV=development

# Run the application
CMD ["python", "main.py"]
