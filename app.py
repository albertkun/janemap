#from config import *
from flask import Flask, render_template,flash, redirect, request, url_for,jsonify,abort,make_response, Response
from models import *
from forms import EventHostingForm
from geocode import geocoder
from flask_marshmallow import Marshmallow
from datetime import datetime
import operator


app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'secret'
ma = Marshmallow(app)


event_types = ['Campaign Office','Official','Canvassing','Phonebanking','Voter Registration','Meeting',
				'Fundraising','Rally','Other']

class EventSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('host_name', 'email', 'event_type','event_date','lat','lon')

user_schema = EventSchema()
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
                setattr(event,theField,field.data)
                print getattr(event,theField)
        app.logger.info(form.data)
        event.save()
        geocoder()
        return redirect(url_for('index'))
    elif request.method =='GET':
        return render_template('host.html', form=form)

@app.route('/')
def index():
	currentDay = datetime.now()
	geoevents = Event.select().where(Event.lat.is_null(False) and Event.event_date > currentDay)
	db.close()
	return render_template('index.html',events=geoevents,event_types=event_types)

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
