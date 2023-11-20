import requests
import random

X_RapidAPI_Key = "4ecf27ffd7mshb9e852ab1af37fbp1d65cbjsn70459f614af5"
def get_date_fact(value = None):
    if value:
        url = f"https://numbersapi.p.rapidapi.com/{value}/date?rapidapi-key={X_RapidAPI_Key}"
        response = requests.get(url)
        date_list = [value, response.text, "date"]
        return date_list
    else:
        random_month = str(random.sample(range(1, 12), 1)).replace("[", "").replace("]", "")
        random_day = str(random.sample(range(1, 31), 1)).replace("[", "").replace("]", "")
        random_date = f"{random_month}/{random_day}"

        while(random_date == "2/31" or random_date == "2/30" or random_date == "4/31" or random_date == "6/31" or random_date == "9/31" or random_date == "11/31"):
            random_month = str(random.sample(range(1, 12), 1)).replace("[", "").replace("]", "")
            random_day = str(random.sample(range(1, 31), 1)).replace("[", "").replace("]", "")
            random_date = f"{random_month}/{random_day}"
        url = f"https://numbersapi.p.rapidapi.com/{random_date}/date?rapidapi-key={X_RapidAPI_Key}"
        response = requests.get(url)
        date_list = [random_date, response.text, "date"]
        return date_list

def get_math_fact(value = None):
    if value:
        url = f"https://numbersapi.p.rapidapi.com/{value}/math?rapidapi-key={X_RapidAPI_Key}"
        response = requests.get(url)
        math_list = [value, response.text, "math"]
        return math_list
    else:
        random_number = str(random.sample(range(1,9999), 1)).replace("[", "").replace("]", "")
        url = f"https://numbersapi.p.rapidapi.com/{random_number}/math?rapidapi-key={X_RapidAPI_Key}"
        response = requests.get(url)
        math_list = [random_number, response.text, "math"]
        return math_list

def get_year_fact(value = None):
    if value:
        url = f"https://numbersapi.p.rapidapi.com/{value}/year?rapidapi-key={X_RapidAPI_Key}"
        response = requests.get(url)
        year_list = [value, response.text, "year"]
        return year_list
    else:
        random_year = str(random.sample(range(1,2024), 1)).replace("[", "").replace("]", "")
        url = f"https://numbersapi.p.rapidapi.com/{random_year}/year?rapidapi-key={X_RapidAPI_Key}"
        response = requests.get(url)
        year_list = [random_year, response.text, "year"]
        return year_list

def get_trivia_fact(value = None):
    if value:
        url = f"https://numbersapi.p.rapidapi.com/{value}/trivia?rapidapi-key={X_RapidAPI_Key}"
        response = requests.get(url)
        trivia_list = [value, response.text, "trivia"]
        return trivia_list
    else:
        random_number = str(random.sample(range(1,9999), 1)).replace("[", "").replace("]", "")
        url = f"https://numbersapi.p.rapidapi.com/{random_number}/trivia?rapidapi-key={X_RapidAPI_Key}"
        response = requests.get(url)
        trivia_list = [random_number, response.text, "trivia"]
        return trivia_list