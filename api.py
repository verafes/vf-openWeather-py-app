import requests
from config import API_KEY, BASE_URL, GEO_END_POINT, WEATHER_END_POINT

GEO_URL = f"{BASE_URL}{GEO_END_POINT}"
WEATHER_URL = f"{BASE_URL}{WEATHER_END_POINT}"


def get_weather(zip_code, country_code = "US"):
    """Fetch weather data based on ZIP code."""
    if not zip_code or zip_code.strip() == "":
        return None, "Please enter a ZIP code"

    geo_params = {
        'zip': f"{zip_code},{country_code}",
        'appid': API_KEY
    }
    geo_response = requests.get(GEO_URL, params=geo_params)

    if geo_response.status_code != 200:
        return None, "Location not found. Please try a different zip code"

    geo_data = geo_response.json()
    lat, lon, city = geo_data["lat"], geo_data["lon"], geo_data["name"]

    weather_url = f"{BASE_URL}{WEATHER_END_POINT}?lat={lat}&lon={lon}&appid={API_KEY}&units=imperial"
    weather_response = requests.get(weather_url)

    if weather_response.status_code != 200:
        return None, "Weather data unavailable"

    weather_data = weather_response.json()
    weather_response.json()

    return {
        "city": city,
        "latitude": lat,
        "longitude": lon,
        "temperature": weather_data["main"]["temp"],
        "description": weather_data["weather"][0]["description"],
        "pressure": weather_data["main"]["pressure"],
        "humidity": weather_data["main"]["humidity"],
        "wind_speed": weather_data["wind"]["speed"],
        "icon": f"http://openweathermap.org/img/wn/{weather_data['weather'][0]['icon']}@2x.png",
    }, None



