import random

class Cell:

    def __init__(self, p: float):

        # Initial state of Cell is set to zero.
        # In the future, should be randomized.
        # Also, encapsulation.
        self._state = 1 if random.random() < p else 0

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state