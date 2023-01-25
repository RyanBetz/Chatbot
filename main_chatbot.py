
class Toggler:
    def __init__(self, *args):
        self.states = args

    def set_state(self, state):
        if state not in self.states:
            raise Exception("Not a valid state")

        self.states.remove(state)
        self.states.append(state)

    def get_state():
        return self.args[-1]

class ChatBot:
    def __init__(self):
        self.conversation_states = Toggler(
            "awaiting_search",
            "narrowing_search",
            "sentiment",
            "visualize"
        )
        self.conversation_states.set_state("awaiting_search")
