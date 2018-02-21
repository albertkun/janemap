from models import Event
import requests
from time import sleep
def geocoder():
    for event in Event.select().where(Event.lat.is_null()):
        print (event)
        if event.geocode_attempt == False:
            try:
                sleep(3)
                # Form the URL with the address in it
                #print str(event.full_address())
                url = "http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address={}".format(event.full_address())

                print (url)
                # Request the URL

                response = requests.get(url)

                # Traverse the Google API JSON to find location geometry array
                coords = response.json()['results'][0]['geometry']['location']

                # Assign the lat/lng into the object (the row)
                event.lat = coords['lat']
                event.lon = coords['lng']
                # And now save it to the database
                #print "{} is at {}, {}".format(event.event_name, event.lat, event.lon)

                event.save()
            except:
              #print "Failed to query/save for {}".format(event.event_name)
              event.geocode_attempt = True
              event.save()
