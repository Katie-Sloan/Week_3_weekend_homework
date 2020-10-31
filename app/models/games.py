from app.models.game import *
from app.models.players import players
from app.models.player import *

# game1 = Game("Fred", "rock", "Wilma", "paper")
games = []
# player1 = Player("Fred", "rock")
# player2 = Player("Wilma", "paper")

def add_game(game):
    games.append(game)