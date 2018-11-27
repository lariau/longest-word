# game.py
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import random
import string

class Game():
    def __init__(self):
        self.grid = []
        for _ in range(0, 9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        for i in range(0, len(word)):
            if list(word)[i] not in self.grid:
                return False
        return True
