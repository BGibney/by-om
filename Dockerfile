# source inspiration https://medium.com/backticks-tildes/how-to-dockerize-a-django-application-a42df0cb0a99

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
# deprecated as it doesn't work on Pi? To be confirmed
#FROM python:3.7-alpine
FROM arm32v6/python:3.7-alpine

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# Copy the project repo to inside the container
COPY /by_om /by_om
# Set the working directory to /by_om
WORKDIR /by_om

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# make port 8080 available
EXPOSE 8080

RUN python manage.py migrate

RUN echo "Test from within the container"

#RUN python manage.py runserver 0.0.0.0:8080
