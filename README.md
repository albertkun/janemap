# janemap
based off of these two tutorials:
http://jonathansoma.com/tutorials/webapps/intro-to-flask/

https://medium.com/@prabhath_kiran/simple-rest-api-using-flask-and-peewee-3d75c7bff515

peewee docs:

http://docs.peewee-orm.com/en/latest/peewee/quickstart.html#model-definition

## step one
pip install virtualenv

pip install virtualenvwrapper (for Linux/Macs)
pip install virtualenvwrapper-win (for windows)

mkvirtualenv flaskmap

workon flaskmap

pip install flask

pip install peewee

pip install psycopg2

## create database

make sure you have a postgresql database up and running by installing postgresql:

https://www.postgresql.org/download/

we will use peewee to connect to the database

store your configurations in a file so that it is not made public in a file like: config.py

## create templates

after connecting to the database we will return the queries as variables and then pass them into our jinja2 templates.

## establish API

we can handle user requests to different endpoint by modifying the routing.

## migrate to production server

depending on the platform, we can either host our app on heroku or on a private webserver running either linux or windows server.
