import os
from flask import Flask, render_template, request, send_from_directory
from api import get_weather
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

app = Flask(__name__, static_folder="static")


@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    error = None
    current_year = datetime.now().year

    if request.method == "POST":
        zip_code = request.form["zipcode"].strip()

        if len(zip_code) == 5 and zip_code.isdigit():
            weather_data, error = get_weather(zip_code)
            print("weather_data", weather_data, error)
        else:
            error = "Please enter a valid 5-digit ZIP code"

    return render_template("weather.html", weather_data=weather_data, error=error, current_year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
