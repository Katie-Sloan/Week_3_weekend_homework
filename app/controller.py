from flask import render_template, request
from app import app
from app.models.game import *
from app.models.player import *

@app.route('/')
def index():
    return render_template('index.html', title="Home")

@app.route('/result', methods=['POST'])
def check_winner():
    player1name = request.form['player1name']
    player2name = request.form['player2name']
    hand1 = request.form['hand1']
    hand2 = request.form['hand2']
    player1 = Player(name=player1name, choice=hand1)
    player2 = Player(name=player2name, choice=hand2)
    game = Game(player1=player1, player2=player2)
    feedback = game.return_winner(player1, player2)
    if game.return_winner(player1, player2) == player1:
        return f"{player1.name} wins! {player1.choice} beats {player2.choice}"
    if game.return_winner(player1, player2) == player2:
        return f"{player2.name} wins! {player2.choice} beats {player1.choice}"
    if game.return_winner(player1, player2) == None:
        return "It's a draw!"
    return render_template('index.html', title='Results', feedback=feedback)   
    