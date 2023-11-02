# Use the official Python 3.8 image as the base image
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /usr/src/app

# Copy the local directory's contents into the container
COPY . .

# Install pip, venv, and create a virtual environment
RUN python3 -m venv venv

# Activate the virtual environment and install requirements from requirements.txt
# Assuming requirements.txt is in the starterkit directory
RUN . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r starterkit/requirements.txt

# Install curl
RUN apt-get update && apt-get install -y curl

# Install Node.js and npm
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs

# Install Flask
RUN . venv/bin/activate && \
    pip install Flask

# # Install Yarn and Gulp
# RUN npm install --global yarn gulp

# # Install dependencies and build assets
# RUN cd starterkit/_keenthemes/tools && \
#     yarn install && \
#     gulp && \
#     cd ../../../

# Make run.sh executable
RUN chmod +x starterkit/run.sh

# run.sh is in the starterkit directory
CMD ["sh", "-c", "cd starterkit && ./run.sh"]