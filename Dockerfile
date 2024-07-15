# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables for Python to run in unbuffered mode
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project into the container
COPY . /app/

# Expose the port that the Django development server will run on (usually 8000)
EXPOSE 8000

# Define the command to run when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
