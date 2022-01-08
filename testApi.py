import requests
import json
import socket

# TIME ZONE API
# place = input("which timezone do u want?\n")

# IANA_options = requests.get("https://www.timeapi.io/api/TimeZone/AvailableTimeZones").json()
# print(IANA_options)
# index = -1

# not_city = ["africa", "america", "antarctica", "asia", "atlantic", "australia", "brazil", "canada", "chile", "etc", "europe", "indian", "mexico", "pacific", "us"]
# #checks the input against each value in the list
# for valid_place in IANA_options:
#     # a value is not in a string if str.find() == -1
#     if valid_place.lower().find(place.lower()) != -1:

#         index = IANA_options.index(valid_place)
#         break
#     else:
#         continue

# #If the place was found in the list, then it's used to fetch the time
# if index >= 0:
#     parameters = {
#         "timeZone": IANA_options[index],
#     }
#     response = requests.get("https://www.timeapi.io/api/Time/current/zone", params=parameters)
    
#     # returns sentence
#     # if user inputs a continent or country, then the first valid answer in the json 
#     # file will be assumed. E.g., instead of America, the bot will respond with America/Adak
#     if place.lower() in not_city:
#         print("the time in", IANA_options[index], "is", response.json()['time'])
#     else:
#         print("the time in", place.capitalize(), "is", response.json()['time'])


# WEATHER API
weather_key = "f5a120d67a0246e2ad311505220801"
# parameters for calling weather json. refer to documentation for "q" since it can hold multiple 
# data types
weather_parameters = {
    "key": weather_key,
    "q": "auto:ip",
}
print(socket.gethostbyname(socket.gethostname()))

# optional parameters include:
# - "hour" ("hour":5 is 5am)
# - "days" ("days":5 is number of days of forecast)
request_weather = requests.get("http://api.weatherapi.com/v1/forecast.json", params=weather_parameters).json()

# collects the location's wind, precipitation, humidity, and average temperature
print(u"""
The weather in {} is {}:
- wind: {} km/h
- precipitation: {} mm
- humidity: {}
- average temperature: {}\N{DEGREE SIGN}C
""".format(request_weather["location"]["name"], request_weather["current"]["condition"]["text"].lower(), request_weather["current"]["wind_kph"], request_weather["current"]["precip_mm"], request_weather["current"]["humidity"], request_weather["current"]["temp_c"]))

print(request_weather)
