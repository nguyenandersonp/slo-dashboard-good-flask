# Use the official Python image as the base image
FROM python:3.10-slim-buster

# Set the working directory
WORKDIR /usr/src/app

# Copy the local directory's contents into the container
COPY . .

# Install Flask, Node.js and Yarn
RUN apt-get update && \
    apt-get install -y nodejs npm && \
    npm install --global yarn && \
    pip install Flask

# Build the assets and run the Flask application
CMD ["sh", "-c", "cd starterkit/_keenthemes/tools && yarn install && npm run build && cd ../../ && python -m flask run"]
