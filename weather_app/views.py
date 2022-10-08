from django.shortcuts import HttpResponse, render
from django.http import HttpResponseBadRequest
import urllib.request
import json




def index(request):

    if request.method == 'POST':

        # replace white space with '%20' for compatibility with API
        city = request.POST['city'].replace(" ", "%20")
        
        # try getting weather data, throw Bad Request if exception
        try:
            response_data = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='
                                            +city+'&units=metric&appid={}').read()
        except Exception:
            return HttpResponseBadRequest("Bad Request")


        response_json = json.loads(response_data)

        
        data = {
            "country_code": str(response_json['name']),
            "temp": str(response_json['main']['temp']) + ' °C',
            "pressure": str(response_json['main']['pressure']),
            "humidity": str(response_json['main']['humidity']),
            'main': str(response_json['weather'][0]['main']),
            'description': str(response_json['weather'][0]['description']),
            'icon': response_json['weather'][0]['icon'],
        }

    else:

        return HttpResponseBadRequest("Bad Request")
    
    return render(request, 'main/index.html', data)
