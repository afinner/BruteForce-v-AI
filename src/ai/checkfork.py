
        

    
def check_fork(board):
    return check_fork_internal(board, 'X')

def block_fork(board):
    return check_fork_internal(board, 'O')

def check_fork_internal(board, p1='O'):
    gridSize = 4
    if p1 == 'X': p2 = 'O'
    else: p2='X'
    """ Check if a corner or an edge square contains a fork opportunity. """
    corners = [(0,0), (gridSize -1, 0), (0, gridSize - 1), (gridSize-1, gridSize - 1)]
    for i, j in corners:
        if (board[i][j] == '_' and
            rCount(board, i, p1) == gridSize - 2 and
            vCount(board, j, p1) == gridSize - 2 and
            rCount(board, i, p2) == 0 and
            vCount(board, j, p2) == 0):
            return i, j
    cornersd1 = [corners[0], corners[3]]
    cornersd2 = [corners[1], corners[2]]
    for i, j in cornersd1:
        if (board[i][j] == '_' and
            rCount(board, i, p1) == gridSize - 2 and
            dCount1(board, gridSize, p1) == gridSize - 2 and
            rCount(board, i, p2) == 0 and
            dCount1(board, gridSize, p2) == 0):
            return i, j
        elif (board[i][j] == '_' and
            dCount1(board, gridSize, p1) == gridSize - 2 and
            vCount(board, j, p1) == gridSize - 2 and
            dCount1(board, gridSize, p2) == 0 and
            vCount(board, j, p2) == 0):
            return i, j
    for i, j in cornersd2:
        if (board[i][j] == '_' and
            rCount(board, i, p1) == gridSize - 2 and
            dCount2(board, gridSize, p1) == gridSize - 2 and
            rCount(board, i, p2) == 0 and
            dCount1(board, gridSize, p2) == 0):
            return i, j
        elif (board[i][j] == '_' and
            dCount2(board, gridSize, p1) == gridSize - 2 and
            vCount(board, j, p1) == gridSize - 2 and
            dCount1(board, gridSize, p2) == 0 and
            vCount(board, j, p2) == 0):
            return i, j
    
    edges = [(i,j) for i in range(gridSize) for j in range(gridSize) if i == 0 or i == gridSize - 1 or j == 0 or j == gridSize - 1 and (i,j) not in corners]
    for i, j in edges:
        if (board[i][j] == '_' and
            rCount(board, i, p1) == gridSize - 2 and
            vCount(board, j, p1) == gridSize - 2 and
            rCount(board, i, p2) == 0 and
            vCount(board, j, p2) == 0):
            return i, j
    return None


def rCount(board, i, player):
    """ Count the number of pieces in the ith row. """
    return board[i].count(player)

def vCount(board, j, player):
    """ Count the number of pieces in the jth column. """
    return [row[j] for row in board].count(player)

def dCount1(board, gridSize, player):
    """ Count the number of pieces in the diagonals. """
    d1_count = [board[i][i] for i in range(gridSize)].count(player)
    return d1_count

def dCount2(board, gridSize, player):
    d2_count = [board[i][gridSize - i - 1] for i in range(gridSize)].count(player)
    return d2_count


def checkFork(board, result):
    print(result)
    if check_fork(board) != result:
        print("test Failed:", board, result)

#def main():
    # checkFork([['X', '_', '_'], ['O','_','X'], ['X', 'O', '_']], (0,2))
    # checkFork([['X', '_', '_'], ['O','_','O'], ['X', 'O', '_']], (0,2))
    # checkFork([['O', '_', 'X'], ['O','_','_'], ['X', '_', '_']], (2,2))
    # checkFork([['X', '_', '_'], ['_','_','X'], ['_', 'O', 'O']], (1,0))
    # checkFork([['O', 'X', 'O'], ['O','_','X'], ['X', '_', '_']], (2,1))
    # checkFork([['X', 'X', 'O'], ['O','_','X'], ['_', 'X', '_']], (2,2))
    # checkFork([
    #     ['X', 'X', '_', '_'],
    #     ['O', '_', 'X', 'X'],
    #     ['X', 'O', '_', '_'],
    #     ['X', 'O', '_', 'X']], (0,3))
    # checkFork([
    #     ['_', 'X', '_', '_'],
    #     ['X', 'X', 'O', 'X'],
    #     ['_', 'O', '_', '_'],
    #     ['X', 'O', '_', 'X']], (0,0))

#main()