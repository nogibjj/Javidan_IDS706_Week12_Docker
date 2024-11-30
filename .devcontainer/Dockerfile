# Use the official Python image as the base image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Install the required Python packages
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 5050

# Set the command to run the Flask app
CMD ["python", "src/main.py"]