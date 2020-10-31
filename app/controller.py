from flask import render_template, request
from app import app
from app.models.players import players
from app.models.game import *
from app.models.games import games
from app.models.player import *

@app.route('/')
def index():
    return render_template('index.html', title="Home")

@app.route('/rock/scissors', methods=['POST'])
def check_winner(): 
    player1name = request.form['player1name']
    player2name = request.form['player2name']
    Katiechoice = request.form['Katiechoice']
    Tomchoice = request.form['Tomchoice']
    player1 = Player(name=player1name, choice=Katiechoice)
    player2 = Player(name=player2name, choice=Tomchoice)
    game = Game(player1=player1, player2=player2)
    return game.return_winner(player1, player2)
    return render_template('index.html', title='Home', feedback=game.return_winner(player1, player2))