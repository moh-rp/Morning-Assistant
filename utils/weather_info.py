import requests
from datetime import datetime


def get_city():
    ip = requests.get("https://ipinfo.io/json")
    location_json = ip.json()
    coords = location_json['loc'].split(',')
    lat = coords[0]
    long = coords[1]
    return lat, long
    

def get_weather(lat, long):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=temperature_2m,precipitation,windspeed_10m&timezone=auto"
    weather = requests.get(url).json()

    now = datetime.now()
    date = now.date()
    current_hour = now.strftime("%H:00")

    morning_index = weather['hourly']['time'].index(f'{date}T{current_hour}')
    noon_index = weather['hourly']['time'].index(f'{date}T{current_hour}')
    evening_index = weather['hourly']['time'].index(f'{date}T{current_hour}')

    print(weather['hourly']['temperature_2m'][morning_index])

    #print(weather)

lat,long=get_city()
get_weather(lat,long)
