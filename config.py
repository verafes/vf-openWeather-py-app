from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')
PEXELS_API_KEY = os.getenv('PEXELS_API_KEY')
BASE_URL="http://api.openweathermap.org"
GEO_END_POINT = "/geo/1.0/zip"
WEATHER_END_POINT = "/data/2.5/weather"
PEXELS_API_URL="https://api.pexels.com"