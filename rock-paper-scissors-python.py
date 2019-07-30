import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round.
Written by: Mohammed Yousef"""

moves = ['rock', 'paper', 'scissors']


class Player():
    # Player class is the parent for all Players in this game
    def __init__(self):  # Initialize a Player instance
        self.score = 0

    def move(self):
        return 'rock'  # The starter Player class always plays 'rock'

    def learn(self, their_move):
        pass


class RandomPlayer(Player):
    # Random player class: chooses its move at random.
    def move(self):
        # Return the player's move random in string
        index = random.randint(0, 2)
        return moves[index]


class ReflectPlayer(Player):
    # Reflect player class: remembers what move the opponent played last round, and plays that move this round.
    def __init__(self):
        # Initialize a ReflectPlayer instance.
        Player.__init__(self)
        self.their_move = None

    def move(self):
        # Return last opponent move in a string.
        if self.their_move is None:
            return Player.move(self)
        return self.their_move

    def learn(self, their_move):
        # Save the move made by the opponent on the last round.
        self.their_move = their_move


class CyclePlayer(Player):
    # Cycle player class: remembers what move it played last round, and cycles through the different moves.
    def __init__(self):
        # Initialize a CyclePlayer instance.
        Player.__init__(self)
        self.last_move = None

    def move(self):
        # Return the player move in a string (cycle).
        move = None
        if self.last_move is None:
            move = Player.move(self)
        else:
            index = moves.index(self.last_move) + 1
            if index >= len(moves):
                index = 0
            move = moves[index]
        self.last_move = move
        return move


class HumanPlayer(Player):
    # Human player class: ask the user to input the move.
    def move(self):
        # Ask the move to the user and return it in a string.
        player_move = input('Enter your move (' +
                            ', '.join(moves) + '):\n')
        while player_move not in moves:
            player_move = input('Invalid move, try again\n')
        return player_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(Player(), Player())
    game.play_game()
