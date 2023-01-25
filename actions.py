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
        # get information from slots
        # 

class GetSubjects(Action):

    def name(self):
        return "get_subjects"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        pass

class SaveResults(Action):

    def name(self):
        return "save_results"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        pass

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
