"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
"""By: Mohammed Yousef"""

"""Rules: (Rock beats Scissors)-(Scissors beats paper)-(Paper beats Rock)"""

import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

class Player():
    def __init__(self):
        self.score = 0

    def move(self):
        return moves[0]

    def learn(self, learn_move):
        pass
# Player class is the parent for all playes

class RandomPlayer(Player):
    def move(self):
        variable = random.choice(moves)
        return (variable)
# RandomPlayer class selects a random move choice

class ReflectPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.learn_move = None

    def move(self):
        if self.learn_move is None:
            variable = moves[0]                      # 1st move: always rock
        else:
            variable = self.learn_move               # Next move: is humanplayers
            return (variable) # Return the previous move                       

    def learn(self, learn_move):
        self.learn_move = learn_move
# ReflectPlayer Class is to reflects the human players 1st and 2nd moves

class Cycles(Player):

    def __init__(self):
        Player.__init__(self)
        self.step = 0

    def move(self):
        variable = None
        if self.step == 0:
            variable = moves[0]
            self.step = self.step + 1
        elif self.step == 1:
            variable = moves[1]
            self.step = self.step + 1
        else:
            variable = moves[2]
            self.step = self.step + 1
        return variable
# move function: for cycles through the moves list starting from rock

class HumanPlayer(Player):
    def move(self):
        variable = input('rock, paper, scissors? >')
        while variable != ('rock' or 'paper' or 'scissors'):
            print('Invalid input try again please')
            variable = input('rock, paper, scissors? >')
        return (variable)
# move function: to ask a human player to select a game
# Then checks user input validation
        
class Game():
    def __init__(self, p2):
        self.p1 = HumanPlayer()
        self.p2 = p2

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print (f"Round {round}:")
            self.play_round()
        if self.p1.score > self.p2.score:
            print('YOU WON!')
        elif self.p1.score < self.p2.score:
            print('Player 2 won!')
        else:
            print('The game was a tie!')
        print('The final score ' + str(self.p1.score) + ' TO ' +
              str(self.p2.score))
# Game class begins the game and prints information
# play_game function Displays informations including final results and announcing the winner

    def play_single(self):
        print("Rock Paper Scissors, LETS GOOOO!")
        print (f"Round 1 of 1:")
        self.play_round()
        if self.p1.score > self.p2.score:
            print('YOU WON!')
        elif self.p1.score < self.p2.score:
            print('Player 2 won!')
        else:
            print('The game was a tie!')
        print('The final score ' + str(self.p1.score) + ' TO ' +
              str(self.p2.score))
# play_single function plays a single round of RPS, similar as play_game function without loop

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        result = Game.play(move1, move2)
        self.p1.learn(move2)
        self.p2.learn(move1)
# This function is to store moves & remember it

    def play(self, move1, move2):
            print(f"You played {move1}")
            print(f"Opponent played {move2}")
            if beats(move1, move2):
                print ("** YOU WON **")
                print(f"Score: You: {move1}  Player 2: {move2}\n\n")
                self.p1.score += 1
                return 1
            elif beats(move2, move1):
                print ("** PLAYER TWO WINS **")
                print(f"Score: You: {move1}  Player 2: {move2}\n\n")
                self.p2.score += 1
                return 2
            else:
                print ("** It's A TIE **")
                print(f"Score: You: {move1}  Player 2: {move2}\n\n")
                return 0
# This function calls the beats function & judging by the rules

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

if __name__ == '__main__':
    pClssList = [Player(), RandomPlayer(), Cycles(), ReflectPlayer()]
    p2 = input('Press Enter for random game\
 or choose: [1]Rock, [2]Random, \
[3]Reflective, or [4]Cycles: >')
    # "pClssList": is a player class list
    # "p2": is output the user entry

    while p2 != 1 or p2 != 2 or p2 != 3 or p2 != 4:
        p2 = random.choice(pClssList)
        break
    # Select rnadom choice if the entry is not one the choices

    if p2 == '1':
        p2 = Player()
    elif p2 == '2':
        p2 = RandomPlayer()
    elif p2 == '3':
        p2 = Cycles()
    elif p2 == '4':
        p2 = ReflectPlayer()
    # Assign p2 to the write player class

    rounds = input('Choose [s] for single game or [f] for full game then Enter: >') 
    Game = Game(p2)
    while True:
        if rounds == 's':
            Game.play_single()
            break
        elif rounds == 'f':
            Game.play_game()
            break
        else:
            print('invalid choice try again please') 
            rounds = input('Enter 1 for a single\
             game and 2 for a full game: >')
    # Request to choose "s"for Single game or "f" for Full
    # Then checks the user's entry