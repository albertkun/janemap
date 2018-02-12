from flask_wtf import FlaskForm
from wtforms import TextField,StringField, DateField,DateTimeField, SelectField,PasswordField
from wtforms.validators import DataRequired, Email

EVENT_TYPES =[("canvass","Canvassing"),("phone","Phone Bank"),
				("voter","Voter Registration"),("meeting","Meeting"),
				("fund","Fundraiser"),("rally","Rally"),("other","Other")]

class EventHostingForm(FlaskForm):
	host_name = TextField("Host Name")
	email = TextField("Email")
	phone = TextField("Phone")
	event_name = TextField("Event Name")
	event_date = DateField("Event Date")
	event_time = TextField("Time")
	# stime = DateTimeField(label='Start time(PST)',validators=[validators.InputRequired()],format = "%H:%M",default= datetime.utcnow)
    # etime = DateTimeField(label='End time(PST)',validators=[validators.InputRequired()],format = "%H:%M",default= datetime.utcnow)	
	event_type = SelectField(label='Event Type', choices=EVENT_TYPES)
	event_description = TextField("Description")
	#neighborhood = TextField("Neighborhood")
	address = TextField("Address")
	city = TextField("City")
	state = TextField("State")