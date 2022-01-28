# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

import requests
import json

from requests.api import request

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionShowTimeZone(Action):
    """Returns the time in another place"""

    # Must return same name as the action
    def name(self) -> Text:
        return "action_show_time_zone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        try:
            # gets the latest entity value from the slots "city". E.g., London. returns None if there's nothing
            place = next(tracker.get_latest_entity_values("city"), None)

            IANA_options = requests.get("https://www.timeapi.io/api/TimeZone/AvailableTimeZones").json()

            #in case user says a continent or country like Australia
            not_city = ["africa", "america", "antarctica", "asia", "atlantic", "australia", "brazil", "canada", "chile", "etc", "europe", "indian", "mexico", "pacific", "us"]
            index = -1

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
                
                    # This returns the message displayed on the screen
                    dispatcher.utter_message(text="The time in {} is {}.".format(IANA_options[index], response.json()['time']))
                    
                    # assigns a found data to a slot. Not usually necessary. E.g., return [SlotSet("matches", result if result is not None else [])]
                    return []

                # Gives time of place
                else:
                    dispatcher.utter_message(text="The time in {} is {}".format(place.capitalize(), response.json()['time']))
                    return []

            # Has an entity but could not retrieve it's corresponding time. For typos
            elif index == -1:
                dispatcher.utter_message(text="Sorry! Looks like I can't find the time in {}. Want to try again?".format(place))
                return []

            # Shouldn't ever run but in case of unexpected value of index arises
            else:
                dispatcher.utter_message(text="Sorry can you repeat that?")
                return []
        except:
            # If API is deprecated or unusable
            dispatcher.utter_message(text="Sorry! It seems like there is an issue with the current time zone APIs. In the meantime, why don't you ask something else?")
            return []

class ActionShowWeather(Action):
    """Returns weather in a place"""
    
    def name(self) -> Text:
        return "action_show_weather"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        try:
            # WEATHER API key
            weather_key = "f5a120d67a0246e2ad311505220801"

            # default is True if no entity is given
            default = False

            place = next(tracker.get_latest_entity_values("city"), None)
            
            if place == None:
                default = True

            IANA_options = requests.get("https://www.timeapi.io/api/TimeZone/AvailableTimeZones").json()

            #in case user says a continent or country like Australia
            not_city = ["africa", "america", "antarctica", "asia", "atlantic", "australia", "brazil", "canada", "chile", "etc", "europe", "indian", "mexico", "pacific", "us"]
            index = -1
        
            if not default:
                #checks the input against each value in the list
                for valid_place in IANA_options:
                    # a value is not in a string if str.find() == -1
                    if valid_place.lower().find(place.lower()) != -1:
                        index = IANA_options.index(valid_place)
                        break

                #If the place was found in the list, then it's used to fetch the time
                if index >= 0:
                    # parameters for calling weather json. refer to documentation for "q" since it can hold multiple 
                    # data types

                    # Gets location if provided
                    weather_parameters = {
                        "key": weather_key,
                        "q": IANA_options[index],
                    }

                    # optional parameters include:
                    # - "hour" ("hour":5 is 5am)
                    # - "days" ("days":5 is number of days of forecast)
                    request_weather = requests.get("http://api.weatherapi.com/v1/forecast.json", params=weather_parameters)
                    
                    text = request_weather.json()["current"]["condition"]["text"].lower()
                    wind = request_weather.json()["current"]["wind_kph"]
                    precipitation = request_weather.json()["current"]["precip_mm"]
                    humidity = request_weather.json()["current"]["humidity"]
                    temperature = request_weather.json()["current"]["temp_c"]

                    if request_weather.status_code != 200:
                        dispatcher.utter_message(text="Sorry! It seems like there is an issue with the current weather APIs. In the meantime, why don't you ask something else?")
                        return []
                
                    # returns first valid city in country as a sentence if the entity is a country or continent
                    elif place.lower() in not_city:
                    
                        # Message displayed on the screen
                        dispatcher.utter_message(text=u"""
                        The weather in {} is {}:
                        - wind: {} km/h
                        - precipitation: {} mm
                        - humidity: {}
                        - average temperature: {}\N{DEGREE SIGN}C
                        """.format(IANA_options[index], text, wind, precipitation, humidity, temperature))

                        return []

                    # Returns weather of place given (if valid)
                    else:
                        dispatcher.utter_message(text=u"""
                        The weather in {} is {}:
                        - wind: {} km/h
                        - precipitation: {} mm
                        - humidity: {}
                        - average temperature: {}\N{DEGREE SIGN}C
                        """.format(place.capitalize(), text, wind, precipitation, humidity, temperature))
                        return []

                # Has an entity but could not retrieve it's corresponding weather
                elif index == -1:
                    # Tries to use the entity given - since the "q" key can take a range of values - before saying 
                    # Information on it doesn't exist
                    try:
                        weather_parameters = {
                        "key": weather_key,
                        "q": place,
                        }

                        request_weather = requests.get("http://api.weatherapi.com/v1/forecast.json", params=weather_parameters)
                        
                        text = request_weather.json()["current"]["condition"]["text"].lower()
                        wind = request_weather.json()["current"]["wind_kph"]
                        precipitation = request_weather.json()["current"]["precip_mm"]
                        humidity = request_weather.json()["current"]["humidity"]
                        temperature = request_weather.json()["current"]["temp_c"]
                        
                        # Reformat it in case the returned value is a capital city
                        if place.lower() != request_weather.json()["location"]["name"].lower():
                            place = str(request_weather.json()["location"]["name"]) + ", " + str(place)
                        
                        dispatcher.utter_message(text=u"""
                        The weather in {} is {}:
                        - wind: {} km/h
                        - precipitation: {} mm
                        - humidity: {}
                        - average temperature: {}\N{DEGREE SIGN}C
                        """.format(place, text, wind, precipitation, humidity, temperature))
                        return []

                    except:
                        dispatcher.utter_message(text="Sorry! Looks like I can't find the weather in {}. Want to try again?".format(place))
                        return []

            # Does not have entity so it's default - accesses weather by IP address. equivalent to elif default
            else:
                # Weather accessed by IP address if no entity exists
                weather_parameters = {
                    "key": weather_key,
                    "q": "auto:ip",
                }
                request_weather = requests.get("http://api.weatherapi.com/v1/forecast.json", params=weather_parameters)
                
                text = request_weather.json()["current"]["condition"]["text"].lower()
                wind = request_weather.json()["current"]["wind_kph"]
                precipitation = request_weather.json()["current"]["precip_mm"]
                humidity = request_weather.json()["current"]["humidity"]
                temperature = request_weather.json()["current"]["temp_c"]
                location = request_weather.json()["location"]["name"]

                dispatcher.utter_message(text=u"""
                According to your IP address, the weather in {} is {}:
                - wind: {} km/h
                - precipitation: {} mm
                - humidity: {}
                - average temperature: {}\N{DEGREE SIGN}C
                """.format(location, text, wind, precipitation, humidity, temperature))
                return []
        except:
            dispatcher.utter_message(text="Oh no! we think our APIs are deprecated. Want to ask another question?")
            return []

class ActionShowDefinition(Action):
    """Returns the definition of a word"""
    # RECOMMENDED TO SURROUND THE WORD IN QUOTES ("") WHEN TYPING
    
    def name(self) -> Text:
        return "action_show_definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        try: 
            # Algorithm to find the word in "". 
            users_message = tracker.latest_message.get('text')
            # gets first "
            start_word = users_message.index("\"") + 1
            users_word = users_message[start_word:]
            # finds second " in start_word
            end_word = users_word.index("\"")

            # actual word we use for definition
            word = users_word[:end_word]
            
            request_word = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(word))
            
            # if request_word.status_code != 200:
            #     dispatcher.utter_message(text="Oh my! It looks like the current dictionary APIs are deprecated...")
            #     return []
            
            request_word = request_word.json()

            definition = False
            example = False

            # First check if word exists, since invalid words have the type dictionary, and valid are in lists
            if isinstance(request_word, dict):
                dispatcher.utter_message(text="Sorry, Scholar! I can't seem to find a definition for {}.".format(word))
                return []
            else:
                # Checking if the word has a definition
                if "definition" in request_word[0]["meanings"][0]["definitions"][0].keys():
                    most_common_definition = request_word[0]["meanings"][0]["definitions"][0]["definition"]
                    definition = True

                # Checking if the word has an example
                if "example" in request_word[0]["meanings"][0]["definitions"][0].keys():
                    example_of_word = request_word[0]["meanings"][0]["definitions"][0]["example"]
                    example = True

                # Prints this if word has both an example and definition
                if definition and example:
                    dispatcher.utter_message(text="""The most common definition of {} is {} For example, {}""".format(word, most_common_definition, example_of_word))
                    return []

                # Prints this if word only has definition
                if definition and not example:
                    dispatcher.utter_message(text="""The most common definition of {} is {} I can't seem to find any examples of this word being used in a sentence...""".format(word, most_common_definition))
                    return []
        
        except:
            dispatcher.utter_message(text="Yikes! It looks like something (our dictionary API) has gone wrong...")
            return []

class ActionShowCountryInfo(Action):
    """Returns the information on a country"""
    
    def name(self) -> Text:
        return "action_find_country_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        try:
            place = next(tracker.get_latest_entity_values("city"), None)
            request_country = requests.get("https://restcountries.com/v3.1/name/{}".format(place)).json()

            if isinstance(request_country, list):
                official_name = request_country[0]['name']['official']
                location_link = request_country[0]['maps']['googleMaps']

                # To get currency for any country. The second part is equivalent to "AUD" in australia
                currency = request_country[0]['currencies'][list(request_country[0]['currencies'].keys())[0]]
                area = request_country[0]['region']
                demonym = request_country[0]['demonyms']['eng']['m']
                population = request_country[0]['population']
                continent = request_country[0]['continents'][0]
                capital = request_country[0]['capital'][0]

                # Again, the second component is specific to each country
                main_language = request_country[0]['languages'][list(request_country[0]['languages'].keys())[0]]

                place = place.capitalize()


                dispatcher.utter_message(text="""
                {}, or officially known as {}, is in the region {} and in the continent {}.
                {}'s currency is the {} ({} {}). Not only that, but did you know there are {} {}s living there at the moment?! 
                Additionally, {}'s Capital is {} with the main language being {}.
                And even though we can't travel there because of COVID, what's stopping us from digitally visiting there with google? {}.
                """.format(place, official_name, area, continent, place, currency['name'], currency['symbol'], list(request_country[0]['currencies'].keys())[0], population, demonym, place, capital, main_language, location_link))
                return []

            else:
                dispatcher.utter_message(text="Oh no! We can't find any info on {}. Have you checked the spelling or made sure you've asked about a country?".format(place))
                return []
        except:
            dispatcher.utter_message(text="Sorry! Something/API has gone wrong...")
            return []

class ActionShowCOVIDData(Action):
    """Returns covid data either globally or for a specific country"""
    
    def name(self) -> Text:
        return "action_find_covid_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        place = next(tracker.get_latest_entity_values("city"), None)
        link = "https://api.covid19api.com/summary"
        request_COVID = requests.get(link).json()

        # Format the date the data was updated nicely
        month_dict = {
            '01':'January',
            '02':'February',
            '03':'March',
            '04':'April',
            '05':'May',
            '06':'June',
            '07':'July',
            '08':'August',
            '09':'September',
            '10':'October',
            '11':'November',
            '12':'December'
            }

        date = request_COVID["Date"]
        year = date[0:4]
        month = month_dict[date[5:7]]
        day = date[8:10]

        # If there was no given entity, bot will assume user wants global data
        if place == None:
            global_new_cases = request_COVID["Global"]["NewConfirmed"]
            global_total_cases = request_COVID["Global"]["TotalConfirmed"]
            global_total_deaths = request_COVID["Global"]["TotalDeaths"]
            global_total_recoveries = request_COVID["Global"]["TotalRecovered"]

            dispatcher.utter_message(text="""
            Today, there were {} confirmed cases globally! In total, there are {} cases, {} deaths, and {} recoveries in the world.
            This data was last updated on {} {}, {}.""".format(global_new_cases, global_total_cases, global_total_deaths, global_total_recoveries, day, month, year))
            return []

        # If user gives an entity, bot will try use it
        elif place != None:
            # Keys are not country names, so I need to identify index of country's info
            list_countries = request_COVID["Countries"]
            country_index = None

            for index in list_countries:
                if place.lower() in index["Country"].lower():
                    country_index = list_countries.index(index)
                    break
                else:
                    continue
            
            # If an index for the country was successfully found, bot will give COVID info on it
            if country_index != None:

                place_new_cases = request_COVID["Countries"][country_index]["NewConfirmed"]
                place_total_cases = request_COVID["Countries"][country_index]["TotalConfirmed"]
                place_total_deaths = request_COVID["Countries"][country_index]["TotalDeaths"]
                place_total_recoveries = request_COVID["Countries"][country_index]["TotalRecovered"]

                dispatcher.utter_message(text="""
                In {}, there were {} cases today! So far, there are {} cases, {} deaths, and {} recoveries in {}.
                This data was last updated on {} {}, {}""".format(place, place_new_cases, place_total_cases, place_total_deaths, place_total_recoveries, place, day, month, year))
                return []

            # In case entity was not a valid value
            elif country_index == None:
                dispatcher.utter_message(text="Uh oh! Looks like I can't find any COVID data for {}. Have you checked the spelling?".format(place))
                return []

class ActionShowCOVIDData(Action):
    """Returns covid data either globally or for a specific country"""

    def name(self) -> Text:
        return "action_find_joke"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Valid categories are: Any, Misc, Programming, Dark, Pun, spooky, christmas. Default settings:
        category = "Programming,Miscellaneous,Pun,Spooky,Christmas"
        blackList = "nsfw,religious,political,racist,sexist,explicit"

        # In GUI, if explicit is on, then
        # blackList = ""
        # category = [options entered]
        # --Shows warning that it could be offensive to the audience--

        # Adjusts request if blackList is empty or not
        if blackList == "":
            request_jokes = requests.get("https://v2.jokeapi.dev/joke/{}".format(category))
        elif blackList != "":
            request_jokes =  requests.get("https://v2.jokeapi.dev/joke/{}?blacklistFlags={}".format(category, blackList))

        # In case API doesn't respond properly
        if request_jokes.status_code != 200:
            dispatcher.utter_message(text="Oops! Something has gone wrong with our Jokes API. Why don't you try something else in the meantime?")
            return []
        
        # Adjusts output depending if there is one or two parts to a joke
        elif request_jokes.json()['type'] == 'twopart':
            setup = request_jokes.json()['setup']
            delivery = request_jokes.json()['delivery']
            dispatcher.utter_message(text="{}\n{}".format(setup, delivery))
            return []

        elif request_jokes.json()['type'] == 'single':
            joke = request_jokes.json()['joke']
            dispatcher.utter_message(text=joke)
            return []