from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import requests
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


class GetTweets(Action):

    def name(self):
        return "get_tweets"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        pass
        # get information on company and query from slots
        # call twitter api on a search string based on company + query
        # format response
        # call dispatcher.utter_message()
        # return SlotSet call?

class GetCompany(Action):

    def name(self):
        return "get_company"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        
        company = tracker.get_slot('company')
        response = f"You chose {company}."
        dispatcher.utter_message(response)
        return [SlotSet("company", company)]

class GetSubjects(Action):

    def name(self):
        return "get_subjects"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        
        subjects = tracker.get_slot('subjects')
        response = f"Here are some subjects related to _company_ that people have been tweeting about:/n {subjects}"
        followup = "What subject do you want to look into more deeply?"

        dispatcher.utter_message(response)
        dispatcher.utter_message(followup)
        # get some kind of input and put it into the 'query' slot

        return [SlotSet("subjects", subjects)]

class SaveResults(Action):

    def name(self):
        return "save_results"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        pass
        
        dispatcher.utter_message("Your data will be saved for later.")

class GetSentiments(Action):

    def name(self):
        return "get_sentiments"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        pass

class GetDataViz(Action):

    def name(self):
        return "get_data_viz"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        pass
