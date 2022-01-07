import requests
import json

place = input("which timezone do u want?\n")

IANA_options = requests.get("https://www.timeapi.io/api/TimeZone/AvailableTimeZones").json()
print(IANA_options)
index = -1

not_city = ["africa", "america", "antarctica", "asia", "atlantic", "australia", "brazil", "canada", "chile", "etc", "europe", "indian", "mexico", "pacific", "us"]
#checks the input against each value in the list
for valid_place in IANA_options:
    # a value is not in a string if str.find() == -1
    if valid_place.lower().find(place.lower()) != -1:

        index = IANA_options.index(valid_place)
        break
    else:
        continue

#If the place was found in the list, then it's used to fetch the time
if index >= 0:
    parameters = {
        "timeZone": IANA_options[index],
    }
    response = requests.get("https://www.timeapi.io/api/Time/current/zone", params=parameters)
    
    # returns sentence
    # if user inputs a continent or country, then the first valid answer in the json 
    # file will be assumed. E.g., instead of America, the bot will respond with America/Adak
    if place.lower() in not_city:
        print("the time in", IANA_options[index], "is", response.json()['time'])
    else:
        print("the time in", place.capitalize(), "is", response.json()['time'])
