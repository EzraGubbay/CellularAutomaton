import random

class Cell:

    def __init__(self):

        # Initial state of Cell is set to zero.
        # In the future, should be randomized.
        # Also, encapsulation.
        self._state = random.choice([0,1])

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state