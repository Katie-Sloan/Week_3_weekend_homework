import unittest

from app.models.game import Game
from app.models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Katie", "paper")
        self.player2 = Player("Tom", "rock")
        self.player3 = Player("Liam", "rock")
        self.player4 = Player("Maria", "scissors")
        self.player5 = Player("Claire", "rock")
        self.player6 = Player("David", "rock")
        self.player7 = Player("John", "rock")
        self.player8 = Player("Peter", "paper")
        self.player9 = Player("Donald", "paper")
        self.player10 = Player("Nancy", "scissors")
        self.player11 = Player("Edwin", "paper")
        self.player12 = Player("Charlie", "paper")
        self.player13 = Player("Fran", "scissors")
        self.player14 = Player("Sarah", "rock")
        self.player15 = Player("Chris", "scissors")
        self.player16 = Player("Bernie", "scissors")
        self.player17 = Player("Tamika", "scissors")
        self.player18 = Player("Jim", "paper")
        self.game1 = Game(self.player1, self.player2)
        self.game2 = Game(self.player3, self.player4)
        self.game3 = Game(self.player5, self.player6)
        self.game4 = Game(self.player7, self.player8)
        self.game5 = Game(self.player9, self.player10)
        self.game6 = Game(self.player11, self.player12)
        self.game7 = Game(self.player13, self.player14)
        self.game8 = Game(self.player15, self.player16)
        self.game9 = Game(self.player17, self.player18)
    
    def test_player1_paper_beats_player2_rock(self):
        self.game1.return_winner(self.player1, self.player2)
        self.assertEqual(self.player1, self.game1.return_winner(self.player1, self.player2))
        
    def test_player1_rock_beats_player_2_scissors(self):
        self.game2.return_winner(self.player3, self.player4)
        self.assertEqual(self.player3, self.game2.return_winner(self.player3, self.player4))

    def test_player_1_rock_draws_with_player_2_rock(self):
        self.game3.return_winner(self.player5, self.player6)
        self.assertEqual(None, self.game3.return_winner(self.player5, self.player6))

    def test_player_1_rock_loses_to_player_2_paper(self):
        self.game4.return_winner(self.player7, self.player8)
        self.assertEqual(self.player8, self.game4.return_winner(self.player7, self.player8))

    def test_player_1_paper_loses_to_player_2_scissors(self):
        self.game5.return_winner(self.player9, self.player10)
        self.assertEqual(self.player10, self.game5.return_winner(self.player9, self.player10))

    def test_player_1_paper_draws_with_player_2_paper(self):
        self.game6.return_winner(self.player11, self.player12)
        self.assertEqual(None, self.game6.return_winner(self.player11, self.player12))

    def test_player_1_scissors_loses_to_player_2_rock(self):
        self.game7.return_winner(self.player13, self.player14)
        self.assertEqual(self.player14, self.game7.return_winner(self.player13, self.player14))

    def test_player_1_scissors_draws_with_player_2_scissors(self):
        self.game8.return_winner(self.player15, self.player16)
        self.assertEqual(None, self.game8.return_winner(self.player15, self.player16))

    def test_player_1_scissors_beats_player_2_paper(self):
        self.game9.return_winner(self.player17, self.player18)
        self.assertEqual(self.player17, self.game9.return_winner(self.player17, self.player18))
