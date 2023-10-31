# Use the official Python image as the base image
FROM python:3.10-slim-buster

# Set the working directory
WORKDIR /usr/src/app

# Copy the local directory's contents into the container
COPY . .

# Install venv and create a virtual environment
# RUN cd starterkit
RUN python -m venv venv
ENV PATH="/usr/src/app/venv/bin:$PATH"

# Install requirements from requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Install Flask, Node.js and Yarn
RUN apt-get update && \
    apt-get install -y nodejs npm && \
    npm install --global yarn && \
    pip install Flask

# Build the assets and run the Flask application
CMD ["sh", "-c", "cd _keenthemes/tools && yarn install && gulp && cd ../../ && chmod +x run.sh && ./run.sh"]
