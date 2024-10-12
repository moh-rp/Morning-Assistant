import requests
from datetime import datetime


def get_coords():
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

    time_index = weather['hourly']['time'].index(f'{date}T{current_hour}')

    current_temp = (weather['hourly']['temperature_2m'][current_temp])
    return current_temp


