#!/usr/bin/python3

import os
import sys

import openweather

api_key = os.environ.get("OPENWEATHER_API_KEY", None)

try:
    ow = openweather.OpenWeather(api_key)
except openweather.OpenWeatherException:
    print("You must set the environmental variable OPENWEATHER_API_KEY")
    sys.exit(1)

data = ow.current_weather_for_city("Skibbereen, ie")

location = data["name"]
weather = data["weather"][0]
print(f"{location}: {weather['main']} - {weather['description']}")

    #function to collect the data from api
    def api_data_collection(api_data = None):
        if api_data == None:
            api_data = []
        city_name = api_driver.find_element_by_xpath()
        api_data.append(city_name.text)
        temp_value = api_driver.find_element_by_xpath()
        #ensuring the temp value doesn't have °C
        api_data.append(temp_value.text[-7:-3])
        humidity_value = api_driver.find_element_by_xpath()
        api_data.append(humidity_value.text)
        return api_data

def difference(locations):

    location = data['city_name']
    temp = data['main']['temp']
    temp[location] = temp

    max = max(temps, temp.get)
    min = min(temps, temp.get)
    diff = temp[max] - current[min]

    print(diff)

def main():
    print(difference())

if __name__ == '__main__':
    main()






