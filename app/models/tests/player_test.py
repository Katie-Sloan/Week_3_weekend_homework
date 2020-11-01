import unittest

from app.models.game import Game
from app.models.player import Player

class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        self.player1 = Player("Katie", "paper")

    def test_player_has_name(self):
        self.assertEqual("Katie", self.player1.name)

    def test_player_has_choice(self):
        self.assertEqual("paper", self.player1.choice)