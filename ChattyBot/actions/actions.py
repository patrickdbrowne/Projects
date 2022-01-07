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

    # Must return same name as the action
    def name(self) -> Text:
        return "action_show_time_zone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        global index

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

            # Has an entity but could not retrieve it's corresponding time
            elif index == -1:
                dispatcher.utter_message(text="Sorry! Looks like   I can't find the time in {}. Want to try again?".format(place))
                return []

            # Does not have time or entity
            else:
                dispatcher.utter_message(text="Sorry can you repeat that?")
                return []
        except:
            dispatcher.utter_message(text="Sorry can you repeat that? Something went wrong!")
            return []

        