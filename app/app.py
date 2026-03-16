from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "45719709a514bb304ff5d8c109387fc1"

@app.route("/", methods=["GET", "POST"])
def index():

    weather = None

    if request.method == "POST":

        city = request.form.get("city")

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:

            weather = {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "description": data["weather"][0]["description"]
            }

        else:

            weather = {
                "city": city,
                "temp": "N/A",
                "description": data.get("message", "API error")
            }

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)