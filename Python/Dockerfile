# Using official python runtime base image
FROM python:3.7.6-alpine

# add apache utils for ab tool
RUN apk update && apk add --no-cache apache2-utils curl

# Set the application directory
WORKDIR /app

# Install our requirements.txt
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy our code from the current folder to /app inside the container
ADD . /app

# Make port 80 available for links and/or publish
EXPOSE 81

# Define our command to be run when launching the container
#CMD ["gunicorn", "sample_file:", "-b", "0.0.0.0:81", "--log-file", "-", "--access-logfile", "-", "--workers", "4", "--keep-alive", "0"]
CMD ["python3", "sample_file.py"]