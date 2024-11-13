# Use the official Python image from the Docker Hub as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt /app/

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code to the working directory
COPY . /app/

# Expose the port that the Flask app will run on
EXPOSE 5000

# Set the environment variable to tell Flask it's in production mode
ENV FLASK_ENV=production

# Set the command to run the application
CMD ["python", "app.py"]
