# Import from peewee
from peewee import *
from models import *
# Connect to the postgresql database

def create_tables():
    with db:
        db.create_tables([People])

create_tables()

