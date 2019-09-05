
# By Om
"By Om" is a web app solution for managing and simulationg biomes
-----

To build and deploy on Raspberry Pi, run the following commands in your terminal:

```

$ sudo docker build https://github.com/CGibney/by-om.git#master -t byom_docker_img:latest

$ sudo docker run -it -p 8080:8080 byom_docker_img:latest python manage.py runserver 0.0.0.0:8080

```

Adapted and inspired from https://github.com/rayed/django_crud







