from flask_wtf import FlaskForm
from wtforms import TextField, StringField, IntegerField, DateField,DateTimeField, SelectField,PasswordField
from wtforms.validators import DataRequired, Email

EVENT_TYPES =[("canvassing","Canvassing"),("phone_banking","Phone banking"),
				("voter_reg","Voter Registration"),("meeting","Meeting"), 
				("fundraiser","Fundraiser"),("rally","Rally"),
				("house_party","House Party"),("forum", "Forum/Discussion"),
				("other","Other")]

class EventHostingForm(FlaskForm):
	host_name = TextField("Host Name")
	email = TextField("Email")
	phone = TextField("Phone")
	event_name = TextField("Event Name")
	event_date = DateField("Event Date")
	start_time = TextField("Start")
	end_time = TextField("End")
	url = TextField("URL")
	max_attendees = IntegerField("max_attendees")
	location_name = TextField("location_name")
	geo_attempt = TextField("geocode_attempt")
	# stime = DateTimeField(label='Start time(PST)',validators=[validators.InputRequired()],format = "%H:%M",default= datetime.utcnow)
    # etime = DateTimeField(label='End time(PST)',validators=[validators.InputRequired()],format = "%H:%M",default= datetime.utcnow)
	event_type = SelectField(label='Event Type', choices=EVENT_TYPES)
	event_description = TextField("Description")
	#neighborhood = TextField("Neighborhood")
	address = TextField("Address")
	city = TextField("City")
	state = TextField("State")

class RSVPform(FlaskForm):
	name = TextField("Host Name")
	email = TextField("Email")
	phone = TextField("Phone")
	event_id = IntegerField("Event_ID")