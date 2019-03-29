# source inspiration https://medium.com/backticks-tildes/how-to-dockerize-a-django-application-a42df0cb0a99

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.7-alpine

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
RUN ls -a

# create root directory for our project in the container
# Unnecessary if your build context is from git?
#RUN mkdir /by_om

#RUN sudo apt-get update \
#   && sudo apt-get install -y git
    
#RUN git clone https://github.com/CGibney/by-om/ by_om


COPY /by_om /by_om
# Set the working directory to /by_om
WORKDIR /by_om


# Install any needed packages specified in requirements.txt
#RUN pip install -r requirements.txt

# make port 8080 available
EXPOSE 8080

RUN python manage.py migrate
RUN python manage.py runserver 0.0.0.0:8080
