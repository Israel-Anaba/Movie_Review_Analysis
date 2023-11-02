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
CMD ["python", "src/app.py"]


