from api import get_url
from datetime import date, timedelta

import json

BASE_URL = "https://api.frankfurter.app"

# Currency API URL
url = BASE_URL + "/currencies" 

# Retrieve list of available currencies from Frankfurter API 
def get_currencies_list(): 
    url = BASE_URL + "/currencies"
    response = get_url(url)
    status_code = response[0]
    text = response[1]
    if status_code == 200:
        data = json.loads(text)
        currency_codes = list(data.keys())
        return currency_codes
    else:
        print("Error", status_code)
        return None

# Retrieve latest exchange rates for selected currencies and amount from Frankfurter API
def get_latest_rates(from_currency, to_currency, amount): 
    url = BASE_URL + "/latest"
    url = url + "?base=" + from_currency
    url = url + "&symbols=" + to_currency
    response = get_url(url)
    status_code = response[0]
    text = response[1]
    if status_code == 200:
        data = json.loads(text)
        date = data["date"]
        rates = data["rates"]
        rate = rates[to_currency]
        return date, rate
    else:
        print("Error", status_code)
        return None, None

# retrieve historical rate from Frankfurter API
def get_historical_rate(from_currency, to_currency, from_date, amount):
    url = BASE_URL + "/" + from_date
    url = url + "?base=" + from_currency
    url = url + "&symbols=" + to_currency
    response = get_url(url)
    status_code = response[0]
    text = response[1]
    if status_code == 200:
        data = json.loads(text)
        date = data["date"]
        rates = data["rates"]
        rate = rates[to_currency]
        return float(rate)
    else:
        print("Error", status_code)
        return None

# retrieve rate trend for selected currencies and years from Frankfurter API
def get_rate_trend(from_currency: str, to_currency: str, years: int) -> dict:
    current_year = date.today().year
    months = [1, 4, 7, 10]
    trend = {}
    for i in range(years):
        year = current_year - i - 1
        for m in months:
            month_text = str(m).zfill(2)
            from_date = str(year) + "-" + month_text + "-01"
            rate = get_historical_rate(from_currency, to_currency, from_date, 1)
            trend[from_date] = rate
    return trend

# retrieve daily rates for selected currencies and years from Frankfurter API
def get_daily_rates(from_currency, to_currency, years=1):
    end_date = date.today()
    start_date = end_date - timedelta(days=years * 365)

    url = BASE_URL + "/" + str(start_date) + ".." + str(end_date)
    url += "?base=" + from_currency
    url += "&symbols=" + to_currency

    response = get_url(url)
    status_code = response[0]
    text = response[1]

    if status_code == 200:
        data = json.loads(text)
        trend = {}

        for day in data["rates"]:
            daily_rates = data["rates"][day]
            trend[day] = daily_rates[to_currency]

        return trend
    else:
        return None
   
    