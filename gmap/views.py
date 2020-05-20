from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.conf import settings

from IPython import embed

import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key=settings.MAP_API_KEY)

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)
embed()

def index(request):
    template = loader.get_template('gmap/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
