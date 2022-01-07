# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

timezones = {
    "London": "UTC+1:00",
    "Sofia": "UTC+3:00",
    "Lisbon": "UTC+1:00",
    "Mumbai": "UTC+5:30"
}
class ActionShowTimeZone(Action):

    # Must return same name as the action
    def name(self) -> Text:
        return "action_show_time_zone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # gets the value of the slots "city". E.g., London
        city = tracker.get_slot("city")

        # gets value of city from record
        timezone = timezones.get(city)

        if timezone is None:
            output = "Could not find the time zone of {}".format(city)
        else:
            output = "The time zone of {} is {}".format(city, timezone)
        
        # This returns the message displayed on the screen
        dispatcher.utter_message(text=output)

        return []
