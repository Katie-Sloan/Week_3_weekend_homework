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
            return self.player2 
        # elif self.player1.choice == "rock" and self.player2.choice == "scissors":
        #     return f"{self.player1.name} wins with {self.player1.choice}!"
        # elif self.player1.choice == "paper" and self.player2.choice == "rock":
        #     return f"{self.player1.name} wins with {self.player1.choice}!"   
        # elif self.player1.choice == "paper" and self.player2.choice == "scissors":
        #     return f"{self.player2.name} wins with {self.player2.choice}!"      
        # elif self.player1.choice == "scissors" and self.player2.choice == "rock":
        #     return f"{self.player2.name} wins with {self.player2.choice}!" 
        # elif self.player1.choice == "scissors" and self.player2.choice == "paper":
        #     return f"{self.player1.name} wins with {self.player1.choice}!" 
        # else:
        #     return "It's a draw!"
    
    def add_game(self, game):
        self.games.append(game)


            # equals thing from last weekend's homework
        
            
    
   

       
   