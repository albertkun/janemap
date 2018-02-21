#from config import *
from flask import Flask, render_template,flash, redirect, request, url_for,jsonify,abort,make_response, Response
from models import *
from forms import EventHostingForm
from geocode import geocoder
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'secret'
ma = Marshmallow(app)


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



            #(event,event[theField],field.data)
            #event.theField=field.data
            #setattr(event[field.name],field.name,field[data])
            # these are available to you:
            # field.name
            # field.description
            # field.label.text
            # field.data
        # print form.event_date.data
        # event.host_name = form.host_name.data
        # event.event_date = form.event_date.data
        # event.event_name = form.event_name.data
        # event.email = form.email.data
        # event.phone = form.phone.data
        # person.uid = time.time()
        app.logger.info(form.data)
        event.save()
        geocoder()
        return redirect(url_for('index'))
    elif request.method =='GET':
        return render_template('host.html', form=form)
  
@app.route('/')
def index():
<<<<<<< HEAD
	currentDay = datetime.now().date()
	eventTypeGroups = (Event.select(Event.event_type)
		.where(Event.event_date >= currentDay)
		.group_by(Event.event_type)
		.having(fn.COUNT(Event.id) != 0))
	geoevents = (Event
		.select()
		.where(Event.lat.is_null(False) and Event.event_date >= currentDay)
		.order_by(Event.event_date.asc()))
	db.close()
	return render_template('index.html',events=geoevents,event_types=event_types,eventTypeGroups=eventTypeGroups)
=======
    geoevents = Event.select().where(Event.lat.is_null(False))
    return render_template('index.html',events=geoevents)
>>>>>>> parent of 4258ae9... Merge pull request #1 from albertkun/searchbox

@app.route('/events/<uid>')
def uid(uid=None):
    events = Event.select().where(Event.uid == uid)
    return render_template('event.html', events=events)  




@app.route("/events/", methods=['GET'])
def get_events():
    all_events = Event.select()
    result = users_schema.dump(all_events)
    return jsonify(result.data)


@app.route('/info')
def info():
  return render_template('info.html', events=events)  

if __name__ == '__main__':
    app.run(debug=True)
