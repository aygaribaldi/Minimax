import copy
import time
import abc
import random


class Game(object):
    """A connect four game."""
    def __init__(self, grid):
        """Instances differ by their board."""
        self.grid = copy.deepcopy(grid)  # No aliasing!

    def display(self):
        """Print the game board."""
        for row in self.grid:
            for mark in row:
                print(mark, end='')
            print()
        print()

    def possible_moves(self):
        """Return a list of possible moves given the current board."""
        moves_list = []
        for row in range(7, -1, -1):
            for col in range(8):
                if self.grid[row][col] == '-' and col not in moves_list:
                    moves_list.append((col))
        # print('MOVES LIST', moves_list)
        moves_list.sort()
        return moves_list

    def neighbor(self, col, color):
        """Return a Game instance like this one but with a move made into the specified column."""
        for r in range(7, -1, -1):
            if self.grid[r][col] == '-':
                self.grid[r][col] = color
                break
        return Game(self.grid)

    def utility(self):
        """Return the minimax utility value of this game"""
        util_val = 0
        # B has 2 in a row
        for r in range(7, -1, -1):
            for c in range(8):
                try:
                    if self.grid[r][c] == '-' and self.grid[r + 1][c] == '-' and self.grid[r + 2][c] == 'B' and \
                            self.grid[r + 3][c] == 'B':
                        util_val += -40
                except:
                    pass
        for r in range(7, -1, -1):
            for c in range(8):
                try:
                    if (self.grid[r][c] == 'B' and self.grid[r][c + 1] == 'B' and self.grid[r][c + 2] == '-' and self.grid[r][c + 3] == '-') or \
                            (self.grid[r][c] == '-' and self.grid[r][c + 1] == 'B' and self.grid[r][c + 2] == 'B' and self.grid[r][c + 3] == '-') or \
                            (self.grid[r][c] == '-' and self.grid[r][c + 1] == '-' and self.grid[r][c + 2] == 'B' and self.grid[r][c + 3] == 'B'):
                        util_val += -40
                except:
                    pass
        for r in range(7, -1, -1):
            for c in range(8):
                try:
                    if (self.grid[r][c] == 'B' and self.grid[r + 1][c + 1] == 'B' and self.grid[r + 2][c + 2] == '-' and \
                            self.grid[r + 3][c + 3] == '-') or (self.grid[r][c] == '-' and self.grid[r + 1][c + 1] == '-' and self.grid[r + 2][c + 2] == 'B' and \
                            self.grid[r + 3][c + 3] == 'B') or (self.grid[r][c] == 'B' and self.grid[r + 1][c + 1] == '-' and self.grid[r + 2][c + 2] == '-' and \
                                    self.grid[r + 3][c + 3] == 'B'):
                        util_val += -40
                except:
                    pass
        for r in range(7, -1, -1):
            for c in range(8):
                try:
                    if (self.grid[r][c] == 'B' and self.grid[r - 1][c + 1] == 'B' and self.grid[r - 2][c + 2] == '-' and \
                            self.grid[r - 3][c + 3] == '-') or (self.grid[r][c] == '-' and self.grid[r - 1][c + 1] == '-' and self.grid[r - 2][c + 2] == 'B' and self.grid[r - 3][c + 3] == 'B') or (self.grid[r][c] == 'B' and self.grid[r - 1][c + 1] == '-' and self.grid[r - 2][c + 2] == '-' and self.grid[r - 3][c + 3] == 'B'):
                        util_val += -40
                except:
                    pass
        # B has 3 in a row
        for r in range(7, -1, -1):
            for c in range(8):
                try:
                    if self.grid[r][c] == '-' and self.grid[r + 1][c] == 'R' and self.grid[r + 2][c] == 'B' and \
                            self.grid[r + 3][c] == 'B':
                        util_val += -100
                except:
                    pass
        for r in range(7, -1, -1):
            for c in range(8):
                try:
                    if (self.grid[r][c] == 'B' and self.grid[r][c + 1] == 'B' and self.grid[r][c + 2] == 'B' and self.grid[r][c + 3] == '-') or \
                            (self.grid[r][c] == 'B' and self.grid[r][c + 1] == 'B' and self.grid[r][c + 2] == 'B' and self.grid[r][c + 3] == '-'):
                        util_val += -100
                except:
                    pass
        for r in range(7, -1, -1):
            for c in range(8):
                try:
                    if self.grid[r][c] == 'B' and self.grid[r + 1][c + 1] == 'B' and self.grid[r + 2][c + 2] == 'B' and \
                            self.grid[r + 3][c + 3] == '-':
                        util_val += -100
                except:
                    pass
        for r in range(7, -1, -1):
            for c in range(8):
                try:
                    if self.grid[r][c] == 'B' and self.grid[r - 1][c + 1] == 'B' and self.grid[r - 2][c + 2] == 'B' and \
                            self.grid[r - 3][c + 3] == '-':
                        util_val += -100
                except:
                    pass

        # R has 2 in a row
        for r in range(7, -1, -1):
            for c in range(8):
                try:
                    if self.grid[r][c] == '-' and self.grid[r + 1][c] == '-' and self.grid[r + 2][c] == 'R' and \
                            self.grid[r + 3][c] == 'R':
                        util_val += 40
                except:
                    pass
        for r in range(7, -1, -1):
            for c in range(8):
                try:
                    if (self.grid[r][c] == 'R' and self.grid[r][c + 1] == 'R' and self.grid[r][c + 2] == '-' and
                        self.grid[r][c + 3] == '-') or \
                            (self.grid[r][c] == '-' and self.grid[r][c + 1] == 'R' and self.grid[r][c + 2] == 'R' and
                             self.grid[r][c + 3] == '-') or \
                            (self.grid[r][c] == '-' and self.grid[r][c + 1] == '-' and self.grid[r][c + 2] == 'R' and
                             self.grid[r][c + 3] == 'R'):
                        util_val += 40
                except:
                    pass
        for r in range(7, -1, -1):
            for c in range(8):
                try:
                    if (self.grid[r][c] == 'R' and self.grid[r + 1][c + 1] == 'R' and self.grid[r + 2][c + 2] == '-' and \
                            self.grid[r + 3][c + 3] == '-') or (self.grid[r][c] == '-' and self.grid[r + 1][c + 1] == '-' and self.grid[r + 2][c + 2] == 'R' and \
                            self.grid[r + 3][c + 3] == 'R') or (self.grid[r][c] == 'R' and self.grid[r + 1][c + 1] == '-' and self.grid[r + 2][c + 2] == '-' and \
                            self.grid[r + 3][c + 3] == 'R'):
                        util_val += 40
                except:
                    pass
        for r in range(7, -1, -1):
            for c in range(8):
                try:
                    if (self.grid[r][c] == 'R' and self.grid[r - 1][c + 1] == 'R' and self.grid[r - 2][c + 2] == '-' and \
                            self.grid[r - 3][c + 3] == '-') or (self.grid[r][c] == '-' and self.grid[r - 1][c + 1] == '-' and self.grid[r - 2][c + 2] == 'R' and \
                            self.grid[r - 3][c + 3] == 'R') or (self.grid[r][c] == 'R' and self.grid[r - 1][c + 1] == '-' and self.grid[r - 2][c + 2] == '-' and \
                            self.grid[r - 3][c + 3] == 'R'):
                        util_val += 40
                except:
                    pass
        # R has 3 in a row
        for r in range(7, -1, -1):
            for c in range(8):
                try:
                    if self.grid[r][c] == '-' and self.grid[r + 1][c] == 'R' and self.grid[r + 2][c] == 'R' and \
                            self.grid[r + 3][c] == 'R':
                        util_val += 100
                except:
                    pass
        for r in range(7, -1, -1):
            for c in range(8):
                try:
                    if (self.grid[r][c] == 'R' and self.grid[r][c + 1] == 'R' and self.grid[r][c + 2] == 'R' and self.grid[r][c + 3] == '-') or \
                            (self.grid[r][c] == '-' and self.grid[r][c + 1] == 'R' and self.grid[r][c + 2] == 'R' and self.grid[r][c + 3] == 'R') or \
                            (self.grid[r][c] == 'R' and self.grid[r][c + 1] == '-' and self.grid[r][c + 2] == 'R' and self.grid[r][c + 3] == 'R') or \
                            (self.grid[r][c] == 'R' and self.grid[r][c + 1] == 'R' and self.grid[r][c + 2] == '-' and self.grid[r][c + 3] == 'R'):
                        util_val += 100
                except:
                    pass
        for r in range(7, -1, -1):
            for c in range(8):
                try:
                    if self.grid[r][c] == 'R' and self.grid[r + 1][c + 1] == 'R' and self.grid[r + 2][c + 2] == 'R' and \
                            self.grid[r + 3][c + 3] == '-':
                        util_val = 100
                except:
                    pass
        for r in range(7, -1, -1):
            for c in range(8):
                try:
                    if self.grid[r][c] == 'R' and self.grid[r - 1][c + 1] == 'R' and self.grid[r - 2][c + 2] == 'R' and \
                            self.grid[r - 3][c + 3] == '-':
                        util_val += 100
                except:
                    pass

        return util_val

    def winning_state(self):
        """Returns float("inf") if Red wins; float("-inf") if Black wins;
           0 if board full; None if not full and no winner"""
        win_val = 0
        # board is not full
        for r in range(7, -1, -1):
            for c in range(8):
                if self.grid[r][c] == '-':
                    win_val = None
                    break
        # R wins
        for r in range(7, -1, -1):
            for c in range(8):
                try:
                    if self.grid[r][c] == 'R' and self.grid[r + 1][c] == 'R' and self.grid[r + 2][c] == 'R' and self.grid[r + 3][c] == 'R':
                        win_val = float('inf')
                except:
                    pass
        for r in range(7, -1, -1):
            for c in range(8):
                try:
                    if self.grid[r][c] == 'R' and self.grid[r][c + 1] == 'R' and self.grid[r][c + 2] == 'R' and self.grid[r][c + 3] == 'R':
                        win_val = float('inf')
                except:
                    pass
        for r in range(7, -1, -1):
            for c in range(8):
                try:
                    if self.grid[r][c] == 'R' and self.grid[r + 1][c + 1] == 'R' and self.grid[r + 2][c + 2] == 'R' and self.grid[r + 3][c + 3] == 'R':
                        win_val = float('inf')
                except:
                    pass
        for r in range(7, -1, -1):
            for c in range(8):
                try:
                    if self.grid[r][c] == 'R' and self.grid[r - 1][c + 1] == 'R' and self.grid[r - 2][c + 2] == 'R' and self.grid[r - 3][c + 3] == 'R':
                        win_val = float('inf')
                except:
                    pass

        # B wins
        for r in range(7, -1, -1):
            for c in range(8):
                try:
                    if self.grid[r][c] == 'B' and self.grid[r + 1][c] == 'B' and self.grid[r + 2][c] == 'B' and \
                            self.grid[r + 3][c] == 'B':
                        win_val = float('-inf')
                except:
                    pass
        for r in range(7, -1, -1):
            for c in range(8):
                try:
                    if self.grid[r][c] == 'B' and self.grid[r][c + 1] == 'B' and self.grid[r][c + 2] == 'B' and \
                            self.grid[r][c + 3] == 'B':
                        win_val = float('-inf')
                except:
                    pass
        for r in range(7, -1, -1):
            for c in range(8):
                try:
                    if self.grid[r][c] == 'B' and self.grid[r + 1][c + 1] == 'B' and self.grid[r + 2][c + 2] == 'B' and self.grid[r + 3][c + 3] == 'B':
                        win_val = float('-inf')
                except:
                    pass
        for r in range(7, -1, -1):
            for c in range(8):
                try:
                    if self.grid[r][c] == 'B' and self.grid[r - 1][c + 1] == 'B' and self.grid[r - 2][c + 2] == 'B' and self.grid[r - 3][c + 3] == 'B':
                        win_val = float('-inf')
                except:
                    pass
        return win_val


class Agent(object):
    """Abstract class, extended by classes RandomAgent, FirstMoveAgent, MinimaxAgent.
    Do not make an instance of this class."""

    def __init__(self, color):
        """Agents use either RED or BLACK chips."""
        self.color = color

    @abc.abstractmethod
    def move(self, game):
        """Abstract. Must be implemented by a class that extends Agent."""
        pass


class RandomAgent(Agent):
    """Naive agent -- always performs a random move"""

    def move(self, game):
        """Returns a random move"""
        move_found = False
        while not move_found:
            rand_move = random.randint(0, 7)
            for i in Game.possible_moves(game):
                if i == rand_move:
                    move_found = True
        return rand_move


class FirstMoveAgent(Agent):
    """Naive agent -- always performs the first move"""

    def move(self, game):
        """Returns the first possible move"""
        move_found = False

        for r in range(7, -1, -1):
            for c in range(8):
                for i in Game.possible_moves(game):
                    if i == c:
                        first_move = c
                        return first_move


class MinimaxAgent(Agent):
    """Smart agent -- uses minimax to determine the best move"""

    def move(self, game):
        """Returns the best move using minimax"""
        minimax_move = self.min_value(game, 4, -1)
        utility = [minimax_move[0]]
        col = minimax_move[1]
        utility.append(float('-inf'))
        best_util = max(utility)
        #print('UTILITY:', best_util, 'COLUMN:', col)
        return col

    def max_value(self, game, depth, col):
        val = []
        # if a state is a completed game, return its utility
        if depth == 1 or game.winning_state() is not None:
            t = (game.utility(), col)
            return t
        # calculate max of min value children
        else:
            v = float('-inf')
            for c in game.possible_moves():
                g1 = Game(game.grid.copy())
                g1.neighbor(c, 'R')
                val.append(self.min_value(g1, depth - 1, c))
            util_vals = [i[0] for i in val]
            util_vals.append(v)
            new_score = max(util_vals)
            col = val[util_vals.index(new_score)][1]
            return [new_score, col]

    def min_value(self, game, depth, col):
        # if a state is a completed game, return its utility
        val = []
        if depth == 1 or game.winning_state() is not None:
            t = (game.utility(), col)
            return t
        # calculate min of max value children
        else:
            v = float('inf')
            for c in game.possible_moves():
                g1 = Game(game.grid.copy())
                g1.neighbor(c, 'B')
                val.append(self.max_value(g1, depth - 1, c))
            util_vals = [i[0] for i in val]
            util_vals.append(v)
            new_score = min(util_vals)
            col = val[util_vals.index(new_score)][1]
            return [new_score, col]


def tournament(simulations=50):
    """Simulate connect four games, of a minimax agent playing
    against a random agent"""

    redwin, blackwin, tie = 0,0,0
    for i in range(simulations):

        game = single_game(io=False)

        print(i, end=" ")
        if game.winning_state() == float("inf"):
            redwin += 1
        elif game.winning_state() == float("-inf"):
            blackwin += 1
        elif game.winning_state() == 0:
            tie += 1

    print("Red %d (%.0f%%) Black %d (%.0f%%) Tie %d" % (redwin,redwin/simulations*100,blackwin,blackwin/simulations*100,tie))

    return redwin/simulations


def single_game(io=True):
    """Create a game and have two agents play it."""

    game = Game([['-' for i in range(8)] for j in range(8)])   # 8x8 empty board
    if io:
        game.display()

    maxplayer = MinimaxAgent('R')
    minplayer = RandomAgent('B')

    while True:

        m = maxplayer.move(game)
        game = game.neighbor(m, maxplayer.color)
        if io:
            time.sleep(1)
            game.display()

        if game.winning_state() is not None:
            break

        m = minplayer.move(game)
        game = game.neighbor(m, minplayer.color)
        if io:
            time.sleep(1)
            game.display()

        if game.winning_state() is not None:
            break

    if game.winning_state() == float("inf"):
        print("RED WINS!")
    elif game.winning_state() == float("-inf"):
        print("BLACK WINS!")
    elif game.winning_state() == 0:
        print("TIE!")

    return game

if __name__ == '__main__':
    single_game(io=True)
    #tournament(simulations=50)