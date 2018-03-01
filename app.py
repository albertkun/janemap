#from config import *
from flask import Flask, render_template,flash, redirect, request, url_for,jsonify,abort,make_response, Response
from models import *
from forms import EventHostingForm,RSVPform
from geocode import geocoder
from flask_marshmallow import Marshmallow
from datetime import datetime
import operator
import sys


app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'secret'
ma = Marshmallow(app)


event_types = ['Campaign Office','Official','Canvassing','Phonebanking','Voter Registration','Meeting',
				'Fundraising','Forum','Meet','Rally','Other']

class EventSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('host_name', 'email', 'event_type','event_date','url','lat','lon')

users_schema = EventSchema(many=True)


global events
events = Event.select().order_by(Event.event_date.asc())

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route("/host/", methods=['GET', 'POST'])
def host():
    form = EventHostingForm(request.form)
    if request.method == 'POST':
        event = Event()
        for field in form:
            if field.name != 'csrf_token':
                print field.name
                theField = str(field.name)
                if field.name == 'event_description':
                    print(sys.stdout.encoding)
                    (field.data).decode('utf-8')
                    print field.data.decode('utf-8')
                setattr(event,theField,field.data)
                #print getattr(event,theField)
        app.logger.info(form.data)
        event.save()
        geocoder()
        return redirect(url_for('index'))
    elif request.method =='GET':
        return render_template('host.html', form=form)




@app.route('/', methods=['GET','POST'])
def index():
    form = RSVPform(request.form)
    currentDay = datetime.now().date()
    eventTypeGroups = (Event.select(Event.event_type)
		.where(Event.event_date >= currentDay)
		.group_by(Event.event_type)
		.having(fn.COUNT(Event.lat) > 0))
    geoevents = (Event
		.select()
		.where(Event.lat.is_null(False) and Event.event_date >= currentDay)
		.order_by(Event.event_date.asc()))
    db.close()
    
    # numberRSVPs = (Event.select(Event.id,fn.COUNT(RSVPs)).where(RSVPs.event_id==Event.id).group_by(Event.id))
    if request.method == 'POST':
        rsvp = RSVPs()
        for field in form:
            print field.name
            theField = str(field.name)
            setattr(rsvp,theField,field.data)
        app.logger.info(form.data)
        rsvp.save()
        # need to add number of rsvps through either updating the event table or feeding it in.
        return redirect(url_for('index'))
    elif request.method =='GET':
	    return render_template('index.html',events=geoevents,event_types=event_types,eventTypeGroups=eventTypeGroups,form=form)

@app.route('/events/<uid>')
def uid(uid=None):
    events = Event.select().where(Event.uid == uid)
    return render_template('event.html', events=events)

@app.route("/events/", methods=['GET'])
def get_events():
    all_events = Event.select()
    result = users_schema.dump(all_events)
    return jsonify(result.data)
    db.close()

@app.route('/info')
def info():
  return render_template('info.html', events=events)

@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()

if __name__ == '__main__':
    app.run(debug=True)
