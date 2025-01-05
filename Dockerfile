# Use a Python base image (we will use Python 3.9 in this case)
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the content of your current directory to /app in the container
COPY . /app

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables to prevent Python from writing pyc files to disk and to avoid buffering of output
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Expose port 8080 (if you want to use it for any web server)
EXPOSE 8080

# Command to run your application
CMD ["python", "hello_vr5.py"]
