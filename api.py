import requests #import requests library

url = "https://api.frankfurter.app/currencies" # Currency API URL

def get_url(url): # Function to get data from API
    response = requests.get(url) # HTTP GET request
    return(response.status_code, response.text) # Return status code and response text