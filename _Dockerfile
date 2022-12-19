# Use an official Python runtime as a base image
FROM python:3.10.8

# Set the working directory to /app
WORKDIR /SWE573

# Copy the current directory contents into the container at /app
COPY . /SWE573

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run manage.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]