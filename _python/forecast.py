# importing modules
import json
import os
import pathlib
from datetime import date

import helper
import requests

# processing
if __name__ == "__main__":
    try:
        root = pathlib.Path(__file__).parent.parent.resolve()

        APIKEY = os.getenv("OPEN_WEATHER_KEY") or ''

        url = ("https://api.openweathermap.org/data/2.5/weather?q=Cheltenham&"
               "s&appid=%s&units=metric" % (APIKEY))

        response = requests.get(url)
        response_dict = json.loads(response.text)

        print(response_dict)

        if response_dict["cod"] != 200:
            string_today = "Weather data not available"
        else:
            d = date.today()
            output_date = d.strftime("%A, %d %B %Y")

            day_temp = str(response_dict["main"]["temp"])
            feels_like = str(response_dict["main"]["feels_like"])
            day_desc = str(response_dict["weather"][0]["description"])

            string_today = f"### on {output_date}\n\n"
            string_today += f"- The average temperature today is {day_temp}˚C,\n"
            string_today += f" but will feel like {feels_like}C with {day_desc}\n"

        f = root / "_pages/morning.md"
        m = f.open().read()
        c = helper.replace_chunk(m, "weather_marker", string_today)
        f.open("w").write(c)
        print("Weather completed")

    except FileNotFoundError:
        print("File does not exist, unable to proceed")