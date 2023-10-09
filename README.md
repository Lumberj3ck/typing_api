
# Typing API

The Typing API is the application interface for a typing trainer built with Vue.js. This submodule provides the necessary backend functionality for the typing trainer. Here are the steps to start and set up the API:

## Getting Started

### Build your container

To get started, you'll need to build a Docker container for the Typing API. Make sure you have Docker and Docker Compose installed.

```
docker-compose build
```
### Start the container
Once the container is built, you can start it using Docker Compose:
```
docker-compose up
```
Note: You might want to change the port in the Docker Compose file from 8000 to 80 to suit your specific requirements. Additionally, you may need to specify your server's public IP address in the env.prod file.
