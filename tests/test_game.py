# tests/test_game.py
import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_game_failure(self):
        new_game = Game()
        new_game.grid = list('KWEUEAKRZ')
        self.assertIs(new_game.is_valid('SANDWICH'), False)
        self.assertEqual(new_game.grid, list('KWEUEAKRZ')) # Make sure the grid remained untouched

    def test_game_success(self):
        new_game = Game()
        new_game.grid = list('KWEUEAKRZ')
        self.assertIs(new_game.is_valid('EUREKA'), True)
        self.assertEqual(new_game.grid, list('KWEUEAKRZ'))

    def test_unknown_word_is_invalid(self):
        new_game = Game()
        new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
        self.assertIs(new_game.is_valid('FEUN'), False)
