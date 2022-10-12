import datetime as dt
import json
import requests
import math 



BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
api_key = "e3c5df87d3fe35ad5e975c028520914c"
city = "Ireland"

response = requests.get(BASE_URL)
 

class OpenWeatherException(Exception):
    pass


class OpenWeather:
    def __init__(self, api_key):
        """Initialize the OpenWeather class with the API key

        Will initialize the OpenWeather class with the API key.  If the API key
        is not set, this will raise a OpenWeatherException
        """

        if api_key is None:
            raise OpenWeatherException("API key not set")

        self.api_key = api_key


    def current_weather_for_city(self, city):
        """Get current weather for a city

        Will return a dictionary with the current weather for a city.
        Currently does not handle API errors gracefully, so it's up to the
        calling application to detect 401s or the like.
        """

        url = f"{BASE_URL}/weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        return json.loads(response.text)

    def get_weather(self, api_key):

        url = f"{BASE_URL}/weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url).json() #returns response

        temp = json['main']['temp']
        temp = math.floor((temp * 1.8) - 459.67) #converts to fahrenheit

        humidity = json['main']['humidity']

        if response.status_code != 200: #check if the weather api key is working

            data = response.json()
            weather = data['weather'][0]['description']
            print("Weather:", weather)
            temperature = round(data["main"]["temp"] - 273.15, 2)
            print("Temperature:", temperature, "celsius")

        if response.json()['count'] == 0: 

            print("An error occurred.") 


    def main():
        city = user_input()
        BASE_URL = get_url(city)
        json = get_json(url)

    



    


        
    