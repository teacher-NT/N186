
"""Minimal ob-havo Funksiyasi"""

import requests
import json

def get_weather(city):
    # Koordinatalarni olish
    geo_url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json&limit=1"
    geo_response = requests.get(geo_url, headers={'User-Agent': 'WeatherApp'}, timeout=10)
    geo_data = geo_response.json()
    
    if not geo_data:
        return {"error": "Shahar topilmadi"}
    
    lat, lon = geo_data[0]['lat'], geo_data[0]['lon']
    
    # Ob-havo ma'lumotlarini olish
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m,precipitation,weather_code&timezone=auto"
    weather_response = requests.get(weather_url, timeout=10)
    weather_data = weather_response.json()
    
    # Natijani JSON ko'rinishida qaytarish
    current = weather_data['current']
    result = {
        "shahar": city,
        "harorat": current['temperature_2m'],
        "namlik": current['relative_humidity_2m'],
        "shamol_tezligi": current['wind_speed_10m'],
        "yogingarchilik": current['precipitation']
    }
    
    return result

city = input("Shahar nomini kiriting: ")
result = get_weather(city)
print(result)