from app.models.player import *

class Game():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.games = []

    # katie = Player(player1name, Katiechoice)
    # tom = Player(player2name, Tomchoice)
    
    # player1 = Player("Fred", "rock")
    # player2 = Player("Wilma", "paper")
    players = []

    
    
    def return_winner(self, player1, player2):
        if self.player1.choice == "rock" and self.player2.choice == "paper":
            return f"{self.player2.name} wins with {self.player2.choice}!"
    
    def add_game(self, game):
        self.games.append(game)


            # equals thing from last weekend's homework
        
            
    
    # def check_winner(katie, tom):
    #     if katie.choice == "rock" and tom.choice == "paper":
    #         return f"{tom.name} wins with {tom.choice}!"
    #     elif Katiechoice == "rock" and Tomchoice == "scissors":
    #         return "Player 1 wins!"
    #     elif Katiechoice == "paper" and Tomchoice == "rock":
    #         return "Player 1 wins!"   
    #     elif Katiechoice == "paper" and Tomchoice == "scissors":
    #         return "Player 2 wins!"     
    #     elif Katiechoice == "scissors" and Tomchoice == "rock":
    #         return "Player 2 wins!"
    #     elif Katiechoice == "scissors" and Tomchoice == "paper":
    #         return "Player 1 wins!"
    #     if:
    #         return "It's a draw"

       
   