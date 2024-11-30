
# Flask Countdown App

This is a simple Flask application that provides a countdown functionality.

## Features

- Countdown timer with customizable time duration.
- Clean and intuitive user interface.
- Dockerized for easy deployment and portability.

## Prerequisites

- Docker installed on your system.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/flask-countdown-app.git
   cd flask-countdown-app
   ```

2. Build the Docker image:

   ```bash
   docker build -t flask-countdown-app -f .devcontainer/Dockerfile .
   ```

3. Run the Docker container:

   ```bash
   docker run -p 5050:5050 flask-countdown-app
   ```

4. Access the application in your browser at: `http://localhost:5050`.

## Directory Structure

- `app/`: Contains the main Flask application code.
- `.devcontainer/`: Includes the Dockerfile and other Docker-related configurations.
- `README.md`: Documentation for the project.

## Deployment

### Using Docker

- **Build Image:**

  ```bash
  docker build -t flask-countdown-app -f .devcontainer/Dockerfile .
  ```

- **Run Container:**

  ```bash
  docker run -p 5050:5050 flask-countdown-app
  ```

## Screenshots

### Home Page
![Home Page](https://github.com/nogibjj/Javidan_IDS706_Week12_Docker/blob/911d8236ef7b5200ed9eed0f25a49bb2bdb2728f/img/app_screenshot.png)


#