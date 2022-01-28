from typing import List
from urllib import request
import requests
import json
import socket

# from requests.api import request

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


# # WEATHER API
# weather_key = "f5a120d67a0246e2ad311505220801"
# # parameters for calling weather json. refer to documentation for "q" since it can hold multiple 
# # data types
# weather_parameters = {
#     "key": weather_key,
#     "q": "Papua New Guinea",
# }
# print(socket.gethostbyname(socket.gethostname()))

# # optional parameters include:
# # - "hour" ("hour":5 is 5am)
# # - "days" ("days":5 is number of days of forecast)
# request_weather = requests.get("http://api.weatherapi.com/v1/forecast.json", params=weather_parameters).json()

# # collects the location's wind, precipitation, humidity, and average temperature
# print(u"""
# The weather in {} is {}:
# - wind: {} km/h
# - precipitation: {} mm
# - humidity: {}
# - average temperature: {}\N{DEGREE SIGN}C
# """.format(request_weather["location"]["name"], request_weather["current"]["condition"]["text"].lower(), request_weather["current"]["wind_kph"], request_weather["current"]["precip_mm"], request_weather["current"]["humidity"], request_weather["current"]["temp_c"]))

# print(request_weather)


# DEFINITIONS API

# word = input("definition of word: ")
# request_word = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(word))

# print(request_word.status_code)
# definition = False
# example = False

# # First check if word exists, since invalid words have the type dictionary, and valid are in lists
# if isinstance(request_word, dict):
#     print("Sorry, Scholar! I can't seem to find a definition for {}.".format(word))

# else:
#     # Checking if the word has a definition
#     if "definition" in request_word[0]["meanings"][0]["definitions"][0].keys():
#         most_common_definition = request_word[0]["meanings"][0]["definitions"][0]["definition"]
#         definition = True

#     # Checking if the word has an example
#     if "example" in request_word[0]["meanings"][0]["definitions"][0].keys():
#         example_of_word = request_word[0]["meanings"][0]["definitions"][0]["example"]
#         example = True

#     # Prints this if word has both an example and definition
#     if definition and example:
#         print("""The most common definition of {} is {} For example, {}""".format(word, most_common_definition, example_of_word))

#     # Prints this if word only has definition
#     if definition and not example:
#         print("""The most common definition of {} is {} I can't seem to find any examples...""".format(word, most_common_definition))

# users_message = 'define wagly woo "oha m goha" '
# # gets first "
# start_word = users_message.index("\"") + 1
# users_word = users_message[start_word:]
# # finds second " in start_word
# end_word = users_word.index("\"")

# print(users_word[:end_word])
# make sure place is not None
# place = input("place: ")
# request_country = requests.get("https://restcountries.com/v3.1/name/{}".format(place)).json()

# if isinstance(request_country, list):
#     official_name = request_country[0]['name']['official']
#     location_link = request_country[0]['maps']['googleMaps']

#     # To get currency for any country. The second part is equivalent to "AUD" in australia
#     print(list(request_country[0]['currencies'].keys()))
#     currency = request_country[0]['currencies'][list(request_country[0]['currencies'].keys())[0]]
#     area = request_country[0]['region']
#     demonym = request_country[0]['demonyms']['eng']['m']
#     population = request_country[0]['population']
#     continent = request_country[0]['continents'][0]
#     capital = request_country[0]['capital'][0]

#     # Again, the second component is specific to each country
#     main_language = request_country[0]['languages'][list(request_country[0]['languages'].keys())[0]]

#     place = place.capitalize()


#     print("""
#     {}, or officially known as {}, is in the region {} and in the continent {}.
#     {}'s currency is the {} ({} {}). Not only that, but did you know there are {} {}'s living there at the moment?! 
#     Additionally, {}'s Capital is {} with the main language being {}.
#     And even though we can't travel there because of COVID, what's stopping us from digitally visiting there with google? {}.
#     """.format(place, official_name, area, continent, place, currency['name'], currency['symbol'], list(request_country[0]['currencies'].keys())[0], population, demonym, place, capital, main_language, location_link))

#     print()
# else:
#     print("howdy buddy. We can't find any info on {}".format(place))

# link = "https://api.covid19api.com/summary"

# request_COVID = requests.get(link).json()

# # if place == None
# global_new_cases = request_COVID["Global"]["NewConfirmed"]
# global_total_cases = request_COVID["Global"]["TotalConfirmed"]
# global_total_deaths = request_COVID["Global"]["TotalDeaths"]
# global_total_recoveries = request_COVID["Global"]["TotalRecovered"]
# month_dict = {
#     '01':'January',
#     '02':'February',
#     '03':'March',
#     '04':'April',
#     '05':'May',
#     '06':'June',
#     '07':'July',
#     '08':'August',
#     '09':'September',
#     '10':'October',
#     '11':'November',
#     '12':'December'
#     }

# date = request_COVID["Date"]
# year = date[0:4]
# month = month_dict[date[5:7]]
# day = date[8:10]


# print("""
# Today, there were {} confirmed cases globally! In total, there are {} cases, {} deaths, and {} recoveries in the world.
# This data was last updated on {} {}, {}.""".format(global_new_cases, global_total_cases, global_total_deaths, global_total_recoveries, day, month, year))

# # if place != None
# place = "russia"
# # Keys are not country names, so I need to identify index of country's info
# list_countries = request_COVID["Countries"]
# country_index = None

# for index in list_countries:
#     if place.lower() in index["Country"].lower():
#         country_index = list_countries.index(index)
#         break
#     else:
#         continue

# if country_index != None:

#     # print(request_COVID["Countries"][country_index])
#     place_new_cases = request_COVID["Countries"][country_index]["NewConfirmed"]
#     place_total_cases = request_COVID["Countries"][country_index]["TotalConfirmed"]
#     place_total_deaths = request_COVID["Countries"][country_index]["TotalDeaths"]
#     place_total_recoveries = request_COVID["Countries"][country_index]["TotalRecovered"]
#     print("""
#     In {}, there were {} cases today! So far, there are {} cases, {} deaths, and {} recoveries in {}.
#     This data was last updated on {} {}, {}""".format(place, place_new_cases, place_total_cases, place_total_deaths, place_total_recoveries, place, day, month, year))
# elif country_index == None:
#     print("Uh oh! Looks like I can't find any COVID data for {}. Have you checked the spelling?".format(place))
# import html

# amount = int(input("number of Q's: "))

# link = 'https://opentdb.com/api.php?amount={}&type=boolean'.format(amount)
# trivia_requests = requests.get(link).json()
# for question_number in range(amount):
#     question = html.unescape(trivia_requests['results'][question_number]['question'])
    
#     # replaces these letters with " symbol
#     # letters = "&quot;"
#     # if letters in question:
#     #     while letters in question:
#     #         question = question[question.index(0):question.index(letters)] + "\"" + question[question.index(letters) + 6 :-1]
        
#     print(question, "Is this True or False?")
#     answer = input("").lower()
#     if answer == trivia_requests['results'][question_number]['correct_answer'].lower():
#         print("Correct!")
#     elif answer != trivia_requests['results'][question_number]['correct_answer'].lower():
#         print("Incorrect!")
#         print("The statement was {}".format(trivia_requests['results'][question_number]['correct_answer']))
# print("Thanks for playing!!")

# Defines output to be in a JSON format, rather than XML or JSONP
# Jokes are sources from https://sv443.net/jokeapi/v2/ posted under the MIT License
# Some jokes might be offensive

# Valid categories are: Any, Misc, Programming, Dark, Pun, spooky, christmas. Default settings:
category = "Programming,Miscellaneous,Pun,Spooky,Christmas"
blackList = "nsfw,religious,political,racist,sexist,explicit"

# In GUI, if explicit is on, then
# blackList = ""
# category = [options entered]
# --Shows warning that it could be offensive to the audience--

if blackList == "":
    request_jokes = requests.get("https://v2.jokeapi.dev/joke/{}".format(category))
elif blackList != "":
    request_jokes =  requests.get("https://v2.jokeapi.dev/joke/{}?blacklistFlags={}".format(category, blackList))

# Adjusts output depending if there is one or two parts to a joke
if request_jokes.status_code != 200:
    print("Oops! Something has gone wrong with our Jokes API. Why don't you try something else in the meantime?")

elif request_jokes.json()['type'] == 'twopart':
    setup = request_jokes.json()['setup']
    delivery = request_jokes.json()['delivery']
    print("{}\n{}".format(setup, delivery))

elif request_jokes.json()['type'] == 'single':
    joke = request_jokes.json()['joke']
    print(joke)