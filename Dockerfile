# Use an official Python runtime as a parent image 
FROM python:3.7-slim

# Set the working directory in the container
WORKDIR /app

# Add current directory code to working directory
ADD . /app
RUN pip3 install flask
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the application when the container launches
CMD ["python", "app.py"]
