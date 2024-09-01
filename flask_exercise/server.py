from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    
    # Validate that the input is not empty string or only spaces
    if not bool(city.strip()):
        city = "Ruse"
    
    weather_data = get_current_weather(city=city)

    # Check if the given city is found
    if not weather_data["cod"] == 200:
        return render_template('city_not_found.html')

    return render_template(
        "weather.html",
        title = weather_data.get("name", "N/A"),
        status = weather_data.get("weather", "N/A")[0]["description"].capitalize(),
        temp = f"{weather_data['main']['temp']:.1f}",
        feels_like = f"{weather_data['main']['feels_like']:.1f}",

    )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)