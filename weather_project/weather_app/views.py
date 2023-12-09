#Create the necessary views in the weather/views.py file:
# from django.shortcuts import render
# from django.http import request, HttpResponse
# import requests
# from django.conf import settings

# def home(request):
#     if request.method == 'POST':
#         city = request.POST.get('city')
#         url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.OPENWEATHERMAP_API_KEY}'
#         response = requests.get(url)
#         data = dict(response.json())
#         return render(request, 'weather.html', {
#             'city': data['name'],
#             'main': data['weather'][0]['main'],
#             'temp': data['main']['temp'],
#             'max': data['main']['temp_max'],
#             'min': data['main']['temp_min'],
#             'feels': data['main']['feels_like'],
#         })
#     return render(request, 'index.html', {})

# weatherApp/views.py

# from django.shortcuts import render
# from django.http import request, HttpResponse
# import requests
# from django.conf import settings

# def home(request):
#     if request.method == 'POST':
#         city = request.POST.get('city')
#         url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.OPENWEATHERMAP_API_KEY}'
        
#         try:
#             response = requests.get(url)
#             response.raise_for_status()  # Raise an HTTPError for bad responses
#             data = response.json()

#             # Check if the 'name' key is present in the data
#             if 'name' in data:
#                 return render(request, 'weather.html', {
#                     'city': data['name'],
#                     'main': data['weather'][0]['main'],
#                     'temp': data['main']['temp'],
#                     'max': data['main']['temp_max'],
#                     'min': data['main']['temp_min'],
#                     'feels': data['main']['feels_like'],
#                 })
#             else:
#                 error_message = "City not found. Please enter a valid city name."
#         except requests.exceptions.HTTPError as errh:
#             error_message = f"HTTP Error: {errh}"
#         except requests.exceptions.ConnectionError as errc:
#             error_message = f"Error Connecting: {errc}"
#         except requests.exceptions.Timeout as errt:
#             error_message = f"Timeout Error: {errt}"
#         except requests.exceptions.RequestException as err:
#             error_message = f"An error occurred: {err}"

#         return render(request, 'index.html', {'error_message': error_message})

#     return render(request, 'index.html', {})


# weatherApp/views.py

from django.shortcuts import render
from django.http import request, HttpResponse
import requests
from django.conf import settings

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def home(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.OPENWEATHERMAP_API_KEY}'
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            data = response.json()

            # Check if the 'name' key is present in the data
            if 'name' in data:
                temperature_celsius = kelvin_to_celsius(data['main']['temp'])
                feels_like_celsius = kelvin_to_celsius(data['main']['feels_like'])

                return render(request, 'weather.html', {
                    'city': data['name'],
                    'main': data['weather'][0]['main'],
                    'temp': temperature_celsius,
                    'max': kelvin_to_celsius(data['main']['temp_max']),
                    'min': kelvin_to_celsius(data['main']['temp_min']),
                    'feels': feels_like_celsius,
                })
            else:
                error_message = "City not found. Please enter a valid city name."
        except requests.exceptions.HTTPError as errh:
            error_message = f"HTTP Error: {errh}"
        except requests.exceptions.ConnectionError as errc:
            error_message = f"Error Connecting: {errc}"
        except requests.exceptions.Timeout as errt:
            error_message = f"Timeout Error: {errt}"
        except requests.exceptions.RequestException as err:
            error_message = f"An error occurred: {err}"

        return render(request, 'index.html', {'error_message': error_message})

    return render(request, 'index.html', {})