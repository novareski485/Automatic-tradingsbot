# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies inside the container
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the Python scripts into the container's working directory
COPY . .

# Define the default command to run your bot
CMD ["python", "main.py"]
