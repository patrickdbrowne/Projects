# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

import requests
import json

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

        # gets the latest entity value from the slots "city". E.g., London. returns None if there's nothing
        place = next(tracker.get_latest_entity_values("city"), None)

        IANA_options = requests.get("https://www.timeapi.io/api/TimeZone/AvailableTimeZones").json()

        #in case user says a continent or country like Australia
        not_city = ["africa", "america", "antarctica", "asia", "atlantic", "australia", "brazil", "canada", "chile", "etc", "europe", "indian", "mexico", "pacific", "us"]
        index = -1

        try:
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

                # If API is deprecated or unusable
                if response.status_code != 200:
                    dispatcher.utter_message(text="Sorry! It seems like there is an issue with the current time zone APIs. In the meantime, why don't you ask something else?")
                    return []
            
                # returns sentence
                # if user inputs a continent or country, then the first valid answer in the json 
                # file will be assumed. E.g., instead of America, the bot will respond with America/Adak
                elif place.lower() in not_city:
                
                    # This returns the message displayed on the screen
                    dispatcher.utter_message(text="The time in {} is {}.".format(IANA_options[index], response.json()['time']))
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
            dispatcher.utter_message(text="Sorry can you repeat that? Something went wrong!")
            return []

class ActionShowWeather(Action):
    """Returns weather in a place"""
    
    def name(self) -> Text:
        return "action_show_weather"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

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

        try:
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
                
                    # returns first valid city in country as a sentence from 
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

                dispatcher.utter_message(text=u"""
                        According to your IP address, the weather in {} is {}:
                        - wind: {} km/h
                        - precipitation: {} mm
                        - humidity: {}
                        - average temperature: {}\N{DEGREE SIGN}C
                        """.format(IANA_options[index], text, wind, precipitation, humidity, temperature))
                return []
        except:
            dispatcher.utter_message(text="Sorry can you repeat that? Something went wrong!")
            return []