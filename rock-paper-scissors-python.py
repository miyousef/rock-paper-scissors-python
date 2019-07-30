import random
"""Rock, Paper and Scissors game
written by: Mohammed Yousef
Email: meam3000@gmail.com"""

moves = ['rock', 'paper', 'scissors']


class Player():
    # Player class is the parent for all Players in this game
    def __init__(self):  # Initialize a Player instance
        self.score = 0

    def move(self):
        return 'rock'  # The starter Player class always plays 'rock'

    def learn(self, learn_move):
        pass


class RandomPlayer(Player):
    # Random player class: chooses its move at random.
    def move(self):
        # Return the player's move random in string
        index = random.randint(0, 2)
        return moves[index]


class ReflectPlayer(Player):
    # Reflect player class: remembers opponent's moves
    def __init__(self):
        # Initialize a ReflectPlayer instance.
        Player.__init__(self)
        self.learn_move = None

    def move(self):
        # Return last opponent move in a string.
        if self.learn_move is None:
            return Player.move(self)
        return self.learn_move

    def learn(self, learn_move):
        # Save the move made by the opponent on the last round.
        self.learn_move = learn_move


class CyclePlayer(Player):
    # Cycle player class: remembers moves & cycles through moves.
    def __init__(self):
        # Initialize a CyclePlayer instance.
        Player.__init__(self)
        self.forward = None

    def move(self):
        move = None
        if self.forward == 0:
            move = moves[0]
            self.forward = self.forward + 1
        elif self.forward == 1:
            move = moves[1]
            self.forward = self.forward + 1
        else:
            move = moves[2]
            self.forward = self.forward + 1
        return move


class HumanPlayer(Player):
    # Human player class: asking user to input the move.
    def move(self):
        # Request user to make a move then return it in a string.
        # pMove: is player move
        pMove = input('rock, paper, scissors? >')

        while pMove != moves[0] and pMove != moves[1] and pMove != moves[2]:
            print('Sorry invalid input, please try again')
            pMove = input('rock, paper, scissors? >')
        return (pMove)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game():
    def __init__(self, p2):
        self.p1 = HumanPlayer()
        self.p2 = p2

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        if self.p1.score > self.p2.score:
            print('1st player wins!')
        elif self.p1.score < self.p2.score:
            print('2nd player wins!')
        else:
            print('It is a tie!')
        print('Final result ' + str(self.p1.score) + ' TO ' +
              str(self.p2.score))
        print("Game over!")

    def play_single(self):
        # play a single round of the game
        print("Rock Paper Scissors, Go!")
        print(f"Round 1 of 1:")
        self.play_round()
        if self.p1.score > self.p2.score:
            print('Player 1 won!')
        elif self.p1.score < self.p2.score:
            print('2nd player wins!')
        else:
            print('It is a tie!')
        print('Final result ' + str(self.p1.score) + ' TO ' +
              str(self.p2.score))
        print("Game over!")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        result = Game.play(move1, move2)
        self.p1.learn(move2)
        self.p2.learn(move1)

    # Display & print results in each round
    def play(self, move1, move2):
        print(f"Your move: {move1}" + ' *** ' + f"Opponent move: {move2}")
        # print(f"Opponent move {move2}")
        if beats(move1, move2):
            print("$$ FIRST PLAYER WINS $$")
            print(f"Result: 1st player: {move1}  2nd player: {move2}\n\n")
            self.p1.score += 1
            return 1
        elif beats(move2, move1):
            print("$$ SECOND PLAYER WINS $$")
            print(f"RESULT: 1st Player: {move1}  2nd Player: {move2}\n\n")
            self.p2.score += 1
            return 2
        else:
            print("$$ It's A TIE $$")
            print(f"RESULT: 1st Player: {move1}  2nd Player: {move2}\n\n")
            return 0
        print("Game over!")


if __name__ == '__main__':
    # gSelect: is game selection
    gSelect = input(
        'Select: [1]Rock, [2]Random, [3]Reflective or [4]CyclePlayer: ')

    # If the entry is not a specific then selects a random choice
    random_Choice = [Player(), RandomPlayer(), CyclePlayer(), ReflectPlayer()]
    while gSelect != 1 or gSelect != 2 or gSelect != 3 or gSelect != 4:
        gSelect = random.choice(random_Choice)
        break

    # Set the p2 variable to the correct player class
    if game_Select == '1':
        game_Select = Player()
    elif game_Select == '2':
        game_Select = RandomPlayer()
    elif game_Select == '3':
        game_Select = CyclePlayer()
    elif game_Select == '4':
        game_Select = ReflectPlayer()

    # Set the length of the game
    rounds = input('Press [s] for single game or [l] for 3 rounds: ')
    Game = Game(game_Select)

    # Validate user inputs
    while True:
        if rounds == 's':
            Game.play_single()
            break
        elif rounds == 'l':
            Game.play_game()
            break
        else:
            print('!Invalid input please try again')
            rounds = input('Press [s] for single game or [l] for long game: ')
