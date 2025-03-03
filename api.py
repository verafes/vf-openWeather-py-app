import requests
import datetime
from config import API_KEY, BASE_URL, GEO_END_POINT, WEATHER_END_POINT, PEXELS_API_KEY, PEXELS_API_URL

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
        return {
            "image_url": f"/static/img/{get_season()}"
        }, "Location not found. Please try a different ZIP code"

    geo_data = geo_response.json()
    lat, lon, city = geo_data["lat"], geo_data["lon"], geo_data["name"]

    weather_url = f"{BASE_URL}{WEATHER_END_POINT}?lat={lat}&lon={lon}&appid={API_KEY}&units=imperial"
    weather_response = requests.get(weather_url)

    if weather_response.status_code != 200:
        return {
            "image_url": f"/static/img/{get_season()}"
        }, "Weather data unavailable"

    weather_data = weather_response.json()
    weather_response.json()

    # Get city image
    image_url = f"{PEXELS_API_URL}/v1/search?query={city}&per_page=1"
    headers = {
        "Authorization": PEXELS_API_KEY
    }
    image_response = requests.get(image_url, headers=headers)

    if image_response.status_code == 200:
        image_data = image_response.json()
        if image_data.get("photos"):
            city_image_url = image_data["photos"][0]["src"]["medium"]
        else:
            city_image_url = f"/static/img/{get_season()}"
    else:
        city_image_url = f"/static/img/{get_season()}"

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
        "image_url": city_image_url,
    }, None

def get_season():
    seasons = {
        (12, 1, 2): "winter.jpg",
        (3, 4, 5): "spring.jpg",
        (6, 7, 8): "summer.jpg",
        (9, 10, 11): "fall.jpg",
    }
    month = datetime.datetime.now().month
    return next(img for months, img in seasons.items() if month in months)

