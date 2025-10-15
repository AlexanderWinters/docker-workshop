# docker-workshop
A workshop on Docker Containers

## Streamlit Hello World App with Docker

This repository contains a simple Streamlit "Hello World" application with Docker containerization for easy deployment.

### What's Included

- **app.py**: A basic Streamlit application that displays a greeting and interactive elements
- **Dockerfile**: Configuration to containerize the Streamlit app
- **requirements.txt**: Python dependencies

### What is the Dockerfile?

The Dockerfile is a script containing instructions to build a Docker image for our Streamlit application. It:

- Uses Python 3.11 slim as the base image
- Sets up the working directory
- Copies application files
- Installs necessary dependencies
- Exposes the default Streamlit port (8501)
- Configures Streamlit to run in headless mode
- Defines the command to start the application

### How to Build and Run

#### Build the Docker Image
```bash
bash docker build -t streamlit-hello-world .
```

#### Run the Container
```bash
docker run -p 8501:8501 streamlit-hello-world
```

After running these commands, access the Streamlit app in your web browser at: http://localhost:8501

### Orchestration / Scaling
In addition to running a container with the `docker run` command, you can also use Docker Compose.
Docker Compose comes together with the Docker Engine. 
You will need a compose file to define the services and their dependencies, instead of running individual commands.
Inspect the `docker-compose.yml` and try deploying: 
```bash
docker compose up
```

### Deployment Options

This containerized application can be deployed to:

- Cloud platforms (AWS, GCP, Azure)
- Kubernetes clusters
- Any environment that supports Docker containers

For production deployment, consider adding:
- Environment configuration
- HTTPS/TLS setup
- Authentication mechanisms
- Container orchestration