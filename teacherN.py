import random
import checkfork

class TeacherN:
    """ 
    A class to implement a teacher that knows the optimal playing strategy.
    Teacher returns the best move at any time given the current state of the game.
    Note: things are a bit more hard-coded here, as this was not the main focus of
    the exercise so I did not spend as much time on design/style. Everything works
    properly when tested.

    Parameters
    ----------
    level : float 
        teacher ability level. This is a value between 0-1 that indicates the
        probability of making the optimal move at any given time.
    """

    def __init__(self, level=0.9, gridSize=3):
        """
        Ability level determines the probability that the teacher will follow
        the optimal strategy as opposed to choosing a random available move.
        """
        self.ability_level = level
        self.gridSize = gridSize
        self.pwin = 0.95
        self.pfork = 0.3
        self.pcenter = 0.5
        self.poffcenter = 0.4
        self.pcorner = 0.8
        self.pside = 0.7

    def win(self, board, key='X'):
        """ If we have two in a row and the 3rd is available, take it. """
        # Check for diagonal wins
        a = []
        b = []
        for i in range(self.gridSize):
            a.append(board[i][i])
            b.append(board[i][self.gridSize-1-i])
        if a.count('_') == 1 and a.count(key) == self.gridSize-1:
            ind = a.index('_')
            return ind, ind
        elif b.count('_') == 1 and b.count(key) == self.gridSize-1:
            ind = b.index('_')
            return ind, self.gridSize-1-ind
        # Now check for 2 in a row/column + empty 3rd
        for i in range(self.gridSize):
            c = []
            d = []
            for j in range(self.gridSize):
                c.append(board[i][j])
                d.append(board[j][i])
            if c.count('_') == 1 and c.count(key) == self.gridSize-1:
                ind = c.index('_')
                return i, ind
            elif d.count('_') == 1 and d.count(key) == self.gridSize-1:
                ind = d.index('_')
                return ind, i
        return None

    def blockWin(self, board):
        """ Block the opponent if she has a win available. """
        return self.win(board, key='O')

    def fork(self, board):
        """ Create a fork opportunity such that we have 2 threats to win. """
        if self.gridSize != 3:
            return checkfork.check_fork(board)
        # Check all adjacent side middles
        if board[1][0] == 'X' and board[0][1] == 'X':
            if board[0][0] == '_' and board[2][0] == '_' and board[0][2] == '_':
                return 0, 0
            elif board[1][1] == '_' and board[2][1] == '_' and board[1][2] == '_':
                return 1, 1
        elif board[1][0] == 'X' and board[2][1] == 'X':
            if board[2][0] == '_' and board[0][0] == '_' and board[2][2] == '_':
                return 2, 0
            elif board[1][1] == '_' and board[0][1] == '_' and board[1][2] == '_':
                return 1, 1
        elif board[2][1] == 'X' and board[1][2] == 'X':
            if board[2][2] == '_' and board[2][0] == '_' and board[0][2] == '_':
                return 2, 2
            elif board[1][1] == '_' and board[1][0] == '_' and board[0][1] == '_':
                return 1, 1
        elif board[1][2] == 'X' and board[0][1] == 'X':
            if board[0][2] == '_' and board[0][0] == '_' and board[2][2] == '_':
                return 0, 2
            elif board[1][1] == '_' and board[1][0] == '_' and board[2][1] == '_':
                return 1, 1
        # Check all cross corners
        elif board[0][0] == 'X' and board[2][2] == 'X':
            if board[1][0] == '_' and board[2][1] == '_' and board[2][0] == '_':
                return 2, 0
            elif board[0][1] == '_' and board[1][2] == '_' and board[0][2] == '_':
                return 0, 2
        elif board[2][0] == 'X' and board[0][2] == 'X':
            if board[2][1] == '_' and board[1][2] == '_' and board[2][2] == '_':
                return 2, 2
            elif board[1][0] == '_' and board[0][1] == '_' and board[0][0] == '_':
                return 0, 0
        return None

    def blockFork(self, board):
        """ Block the opponents fork if she has one available. """
        if self.gridSize != 3:
            return checkfork.block_fork(board)
            
        corners = [board[0][0], board[2][0], board[0][2], board[2][2]]
        # Check all adjacent side middles
        if board[1][0] == 'O' and board[0][1] == 'O':
            if board[0][0] == '_' and board[2][0] == '_' and board[0][2] == '_':
                return 0, 0
            elif board[1][1] == '_' and board[2][1] == '_' and board[1][2] == '_':
                return 1, 1
        elif board[1][0] == 'O' and board[2][1] == 'O':
            if board[2][0] == '_' and board[0][0] == '_' and board[2][2] == '_':
                return 2, 0
            elif board[1][1] == '_' and board[0][1] == '_' and board[1][2] == '_':
                return 1, 1
        elif board[2][1] == 'O' and board[1][2] == 'O':
            if board[2][2] == '_' and board[2][0] == '_' and board[0][2] == '_':
                return 2, 2
            elif board[1][1] == '_' and board[1][0] == '_' and board[0][1] == '_':
                return 1, 1
        elif board[1][2] == 'O' and board[0][1] == 'O':
            if board[0][2] == '_' and board[0][0] == '_' and board[2][2] == '_':
                return 0, 2
            elif board[1][1] == '_' and board[1][0] == '_' and board[2][1] == '_':
                return 1, 1
        # Check all cross corners (first check for double fork opp using the corners array)
        elif corners.count('_') == 1 and corners.count('O') == 2:
            return 1, 2
        elif board[0][0] == 'O' and board[2][2] == 'O':
            if board[1][0] == '_' and board[2][1] == '_' and board[2][0] == '_':
                return 2, 0
            elif board[0][1] == '_' and board[1][2] == '_' and board[0][2] == '_':
                return 0, 2
        elif board[2][0] == 'O' and board[0][2] == 'O':
            if board[2][1] == '_' and board[1][2] == '_' and board[2][2] == '_':
                return 2, 2
            elif board[1][0] == '_' and board[0][1] == '_' and board[0][0] == '_':
                return 0, 0
        return None
        
    def center(self, board):
        """ Pick the center if it is available. """
        if self.gridSize % 2 == 1:
            if board[self.gridSize//2][self.gridSize//2] == '_':
                return self.gridSize//2, self.gridSize//2
        return None

    def offcenter(self, board):
        """ Pick the center if it is available. """
        if self.gridSize % 2 == 0:
            for cr in range(2):
                for cc in range(2):
                    if board[(self.gridSize//2)-1+cr][(self.gridSize//2)-1+cc] == '_':
                        return (self.gridSize//2)-1+cr, (self.gridSize//2)-1+cc
        return None

    def corner(self, board):
        """ Pick a corner move. """
        # Pick opposite corner of opponent if available
        if board[0][0] == 'O' and board[self.gridSize-1][self.gridSize-1] == '_':
            return self.gridSize-1, self.gridSize-1
        elif board[self.gridSize-1][0] == 'O' and board[0][self.gridSize-1] == '_':
            return 0, self.gridSize-1
        elif board[0][self.gridSize-1] == 'O' and board[self.gridSize-1][0] == '_':
            return self.gridSize-1, 0
        elif board[self.gridSize-1][self.gridSize-1] == 'O' and board[0][0] == '_':
            return 0, 0
        # Pick any corner if no opposites are available
        elif board[0][0] == '_':
            return 0, 0
        elif board[self.gridSize-1][0] == '_':
            return self.gridSize-1, 0
        elif board[0][self.gridSize-1] == '_':
            return 0, self.gridSize-1
        elif board[self.gridSize-1][self.gridSize-1] == '_':
            return self.gridSize-1, self.gridSize-1
        return None

    def sideEmpty(self, board):
        """ Pick an empty side. """
        for i in range (1,self.gridSize-1,1):
            if board[i][0] == '_':
                return i, 0
            elif board[self.gridSize-1][i] == '_':
                return self.gridSize-1, i
            elif board[i][self.gridSize-1] == '_':
                return i, self.gridSize-1
            elif board[0][i] == '_':
                return 0, i
        return None

    def randomMove(self, board):
        """ Chose a random move from the available options. """
        possibles = []
        for i in range(self.gridSize):
            for j in range(self.gridSize):
                if board[i][j] == '_':
                    possibles += [(i, j)]
        return possibles[random.randint(0, len(possibles)-1)]

    def makeMove(self, board):
        """
        Trainer goes through a hierarchy of moves, making the best move that
        is currently available each time. A touple is returned that represents
        (row, col).
        """
        # Chose randomly with some probability so that the teacher does not always win
        r = random.random()
        if r > self.ability_level:
            return self.randomMove(board)
        # Follow optimal strategy
        if r < self.pwin:
            a = self.win(board)
            if a is not None:
                return a
        if r < self.pwin:
            a = self.blockWin(board)
            if a is not None:
                return a
        if r < self.pfork:
            a = self.fork(board)
            if a is not None:
                return a
        if r < self.pfork:
            a = self.blockFork(board)
            if a is not None:
                return a
        if r < self.pcenter:
            a = self.center(board)
            if a is not None:
                return a
        if r < self.pcorner:
            a = self.corner(board)
            if a is not None:
                return a
        if r > self.poffcenter:
            a = self.offcenter(board)
            if a is not None:
                return a
        if r < self.pside:
            a = self.sideEmpty(board)
            if a is not None:
                return a
        return self.randomMove(board)
