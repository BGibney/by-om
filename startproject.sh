#!/bin/bash

# remote repo url
byom="https://github.com/CGibney/by-om"


# create directory
mkdir -p ~/projects/

# move to it 
cd ~/projects/

# now clone the remote repo
# .gitignore is included from our remote repo
git clone $byom by-om


# checkout the develop branch so that your work and pushes go to branch develop instead of branch master
# (i.e., let me merge your pull requests into master instead)

git checkout develop

# move to the cloned repo's folder
cd ~/projects/by-om/

# install and init your virtual environment for Django
sudo pip install virtualenv
virtualenv venv && source venv/bin/activate
# install django
pip install django
# start the project and name it by_om
django-admin startapp by_om

# TODO: concatenate the string "localhost" inside the settings.py file, under the line that begins with ALLOWED_HOSTS


# now, migrate the manage.py file
cd by_om/
python manage.py migrate

# start the server and you're good!
python manage.py runserver 0.0.0.0:8080








