# Import from peewee
from peewee import *
from flask import session

from config import Config
# Connect to the PostgresqlDatabase

# for local connecting purposes
# db = PostgresqlDatabase('janemap', user='postgres', password='password',
                           # host='127.0.0.1', port=5432)

db = PostgresqlDatabase(database=Config.DATABASE, user=Config.USERNAME, password=Config.SECRET_KEY,
                          host=Config.HOST, port=Config.PORT)
# Connect to our database.
db.connect()



class People(Model):
    uid = CharField()
    first_name = CharField()
    last_name = CharField()
    email = CharField()
    phone = CharField()
   #event_username = TextField("User Name")
   #password = TextField("User Name")

    def full_name(self):
        return "{} {}".format(self.first_name,self.last_name)

    class Meta:
    # data is coming from schools.db
        database = db
        db_table = 'people'

# Define what a 'Event' is
class Event(Model):
	# These are all the fields it has
	# match up CharField/IntegerField/etc with correct type
	#uid = CharField(primary_key=True) # primary key = unique id
	id = IntegerField(primary_key=True)
	host_name = CharField()
	email = CharField()
	phone = CharField()
	event_name = CharField()
	event_date = DateTimeField()
	start_time = CharField()
	end_time = CharField()
	event_type = CharField()
	event_description = CharField(null = True)
	neighborhood = CharField(null = True)
	address = CharField()
	city = CharField()
	state = CharField()
	zipcode = FixedCharField(null = True,max_length=5)
	attendees = IntegerField(null = True)
	url = CharField()
	lat = DecimalField(null = True)
	lon = DecimalField(null = True)
	geocode_attempt = BooleanField(default=False)

	def full_address(self):
		return "{}, {}, {}".format(self.address,self.city,self.state)

	class Meta:
		# data is coming from schools.db
		database = db
		# and it's in the table called 'events'
		db_table = 'events'
		primary_key = False
