# importing modules
import json
import random
import re
from datetime import datetime, timedelta
import feedparser
from yahoo_fin import stock_info as si
import yfinance as yf
from requests.exceptions import JSONDecodeError
import requests
from bs4 import BeautifulSoup
import pathlib
import yaml


# methods
def add_suffix(day):
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
    return suffix


def format_date(date):
    suffix = add_suffix(date.day)
    formatted_date = date.strftime(f'%A %d{suffix} %B %Y')
    return formatted_date


def load_film_file(file_path):
    path = pathlib.Path(file_path)
    with path.open("r") as f:
        data = yaml.safe_load(f)
    return data


def make_film_url(film_name, apikey):
    url = f"https://www.omdbapi.com/?t={film_name}&r=json&apikey={apikey}"
    return url


def add_film_to_list(film_data, rating, output_file):
    film_code, film_title, film_year = film_data
    film = {
        "Imdb": film_code,
        "Title": film_title,
        "Year": film_year,
        "Rating": rating
    }
    new_films = load_film_file(output_file)
    for f in new_films:
        if f["Imdb"] == film_code:
            return False
    new_films.append(film)
    with pathlib.Path(output_file).open("w") as f:
        yaml.dump(new_films, f)
    return True


def get_film_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data.get("Response") == "True":
            print(f"Found film: {data.get('Title')} ({data.get('Year')})")
            return data.get("imdbID"), data.get("Title"), data.get("Year")
        else:
            print(f"Error: {data.get('Error')}")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except ValueError:
        print("Error: Unable to parse JSON response")
    return None


def get_fixtures(link):
    page = requests.get(link)
    today = format_date(datetime.now())
    tomorrow = format_date(datetime.now() + timedelta(days=1))
    content = re.search(f'{today}(.*?){tomorrow}', page.text,
                        re.DOTALL).group(1)
    soup = BeautifulSoup(content, 'html.parser')
    body_text = ' - '.join(soup.stripped_strings)
    matches = []
    for line in body_text.split(' - '):
        if ' v ' in line:
            matches.append(line)
    if not matches:
        return "No Fixtures"
    return matches


def get_countdown_number_selection():
    selected = list()
    small_numbers = list(range(1, 10)) * 2
    big_numbers = [10, 25, 50, 75, 100]
    random_index = random.randint(1, 4)
    remaining_numbers = 6 - random_index

    for i in range(remaining_numbers):
        selected.append(random.choice(small_numbers))

    for i in range(random_index):
        picked = random.choice(big_numbers)
        big_numbers.remove(picked)
        selected.append(picked)

    return sorted(selected)


def replace_chunk(content: str, m: str, c: str) -> str:
    """Injects content into a template marker"""
    replacer = re.compile(
        r"<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->".format(m, m),
        re.DOTALL,
    )
    c = "<!-- {} starts -->\n{}\n<!-- {} ends -->".format(m, c, m)
    return replacer.sub(c, content)


def remove_img_tags(data: str) -> str:
    """Removes img tags from a string"""
    p = re.compile(r"<img.*?/>")
    return p.sub("", data)


def get_ordinal_string(n: int) -> str:
    """Returns the ordinal of a number"""
    return str(n) + ("th" if 4 <= n % 100 <= 20 else {
        1: "st",
        2: "nd",
        3: "rd"
    }.get(n % 10, "th"))


def stylish_datetime(dt, f):
    """Returns a more stylish datetime format"""
    return dt.strftime(f).replace("{th}", get_ordinal_string(dt.day))


def pretty_print(string: str) -> str:
    """Pretty prints a string"""
    json_formatted_str = json.dumps(string, indent=2)
    return json_formatted_str


def fetch_cfc_entries(url: str) -> list:
    """Fetches CFC entries from a given url"""
    entries = feedparser.parse(url)["entries"]
    return [{
        "title": entry["description"].replace("|", "-"),
        "url": entry["link"].split("#")[0],
        "published": convert_cfc_date(entry["published"]),
    } for entry in entries]


def convert_cfc_date(input: str) -> str:
    """Converts CFC's standard date format to a more readable format"""
    working = datetime.strptime(input, "%a, %d %b %Y %H:%M:%S %z")
    output = datetime.strftime(working, "%d %b")
    return output


def get_yf_stocks(set_of_tickers: list) -> str:
    """Returns a string of stock prices for a given set of tickers"""
    markdown = ""
    for ticker in list(set_of_tickers):
        data = yf.Ticker(ticker)
        output = data.history(period="1d").Close[0]
        markdown += f"- {ticker} : {output} \n"
    return markdown


def get_si_stocks(stocks_list):
    markdown = ""
    for ticker in stocks_list:
        try:
            price = round(si.get_live_price(ticker), 5)
            markdown += f"- {ticker} : {price}\n"
        except JSONDecodeError as e:
            print(f"Error fetching data for {ticker}: {e}")
            markdown += f"- {ticker} : Error fetching data\n"
        except Exception as e:
            print(f"An unexpected error occurred for {ticker}: {e}")
            markdown += f"- {ticker} : Error fetching data\n"
    return markdown


def get_day_of_the_week(today: datetime) -> str:
    """Returns the day of the week"""
    return today.strftime("%A")


def get_week_number(value: datetime) -> int:
    """Returns the week number of a given date"""
    return value.isocalendar()[1]


def is_odd_number(number: int) -> bool:
    """Returns true if a number is odd"""
    if number % 2 == 0:
        return False
    return True


def is_week_one(week: int) -> bool:
    """Returns true if a number is odd"""
    if is_odd_number(week):
        return True
    return False


def is_week_two(week: int) -> bool:
    """Returns true if a number is even"""
    if is_odd_number(week):
        return False
    return True


def is_monday(today) -> bool:
    """Returns true if a date is Monday"""
    return get_day_of_the_week(today) == "Monday"


def is_tuesday(today) -> bool:
    """Returns true if a date is Tuesday"""
    return get_day_of_the_week(today) == "Tuesday"


def is_saturday(today) -> bool:
    """Returns true if a date is Saturday"""
    return get_day_of_the_week(today) == "Saturday"


def is_garden_waste_day(today) -> bool:
    """Returns true if a date is Tuesday and is week two"""
    if is_monday(today) and is_week_two(get_week_number(today)):
        return True
    return False


def is_recycling_waste_day(today) -> bool:
    """Returns true if a date is Tuesday and is week one"""
    if is_tuesday(today) and is_week_one(get_week_number(today)):
        return True
    return False


def is_refuse_waste_day(today) -> bool:
    """Returns true if a date is Tuesday and is week two"""
    if is_tuesday(today) and is_week_two(get_week_number(today)):
        return True
    return False


def is_water_the_plants_day(today) -> bool:
    """Returns true if a date is Saturday and is week two"""
    if is_saturday(today) and is_week_two(get_week_number(today)):
        return True
    return False


def create_date(input: str) -> datetime:
    """Returns a datetime object from a string"""
    return datetime.strptime(input, "%Y-%m-%d")


def get_random_items_from_a_list(out: str, items: list, count: int) -> str:
    """Returns a string of random items from a list"""
    for item in random.sample(items, count):
        out += f"- {item}\n"
    return out


def get_random_quote_from_a_list(out: str, items: list, count: int) -> str:
    """Returns a markdown formatted string of random item from a list"""
    for item in random.sample(items, count):
        out += f"{item}\n"
    return out
