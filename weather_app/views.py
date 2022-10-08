from django.shortcuts import HttpResponse, render
import urllib.request
import json

from django.http import Http404, HttpResponseBadRequest



def index(request):
    if request.method == 'POST':
        city = request.POST['city'].replace(" ", "%20")
        
        try:
            source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='
                                        +city+'&units=metric&appid={}').read()
        except Exception:
            return HttpResponseBadRequest("No Such City Found")


        list_of_data = json.loads(source)

        print(list_of_data)

        data = {
            "country_code": str(list_of_data['name']),
            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}
    
    return render(request, 'main/index.html', data)
