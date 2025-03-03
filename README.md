# Weather in Your City 
A simple Flask web app to fetch weather data using OpenWeatherMap APIs.

## Features
- Fetches weather data from the openWeather API.
- Displays current weather conditions for a specified city.
- Supports multiple cities within the USA.
- Uses OpenWeatherMap Geocoding API and Weather API.

## Technologies Used
### Frontend  
- **HTML** – Structure of the web pages.  
- **CSS** – Styling for a clean user interface.  

### Backend  
- **Python** – Main programming language.  
- **Flask** – Web framework to handle requests and responses.  
- **Flask-CORS** – Enables Cross-Origin Resource Sharing (CORS).  

### APIs & External Services  
- **OpenWeatherMap API** – Fetches weather and geolocation data.  
- **Requests Library** – Handles API requests.  


## Project Structure

The project is structured as follows:

```
:weather_app/
├── static/                # Static files (CSS, JS, images)
│   └── css/
│       └── style.css      # Styling for the web page
├── templates/
│   └── weather.html       # Main template for weather display
├── api.py                 # Functions to fetch coordinates and weather data
├── app.py                 # Main application file
├── config.py              # Configuration settings (e.g., API key)
├── requirements.txt       # List of Python dependencies
└── README.md              # Project documentation
```

## Setup

1. Clone the repository.
2. Create a Virtual Environment `python -m venv venv`
3. Install Python dependencies: `pip install -r requirements.txt`
4. Get an API key from [OpenWeatherMap](https://openweathermap.org/).
5. Add your OpenWeather API key to config.py:
    ```
    API_KEY = "your_api_key_here"
    ```
   
## Usage
1. Run the app: `flask run`
2. Visit `http://127.0.0.1:5000/` in your browser.
3. Enter a 5-digit ZIP code  to get current weather details.
4. View weather details or error messages if the input is invalid.

## License
This project is licensed under the MIT License.