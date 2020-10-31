import unittest

from app.models.game import Game
from app.models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Katie", "rock")
        self.player2 = Player("Tom", "paper")
        self.game = Game(self.player1, self.player2)

    def test_game_can_be_added(self):
        self.game.games.append(self.game)
        self.assertEqual(1, len(self.game.games))
    
    def test_paper_beats_rock(self):
        self.game.return_winner(self.player1, self.player2)
        self.assertEqual(f"{self.player2.name} wins with {self.player2.choice}!", self.game.return_winner(self.player1, self.player2))