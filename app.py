from flask import Flask, render_template, request, jsonify
import requests, json

app = Flask(__name__)

@app.route("/")
def index():
    with open('data.json', 'r') as data:
        return data.json()

#route requires cityname and mood
@app.route("/<city>/<mood>/<key>")
def set_mood(city, mood, key):
    weather = requests.get(f'api.openweathermap.org/data/2.5/weather?q={city}&appid={key}')

    with open('data.json', 'w') as data:
        clean_data = data.json()
        clean_data['entries'].append((city, weather, mood))
        json.dumps(clean_data, data)

    return 200
if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')