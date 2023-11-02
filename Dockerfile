# Use the official Python base image for FastAPI
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app


# Copy the requirements file into the container
COPY ./requirements.txt /app


# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the entire src directory into the container
COPY ./src  /app/src

# Expose the port that your Gradio app will run on
EXPOSE 7860

# # Define the command to run your Gradio application
# CMD ["python", "app.py"]
CMD ["python", "src/app.py"]


# # Use the official Python base image for FastAPI
# FROM python:3.11-slim

# # Set the working directory in the container
# WORKDIR /app

# # Copy the requirements file into the container at /app
# COPY requirements.txt /app/

# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the entire source code from your local "src" directory to the container
# COPY src/ /app/

# # Make port 7860 available to the world outside this container
# EXPOSE 7860

# Define the command to run your Gradio application
# CMD ["python", "app.py"]

# CMD ["python", "src/app.py"]

