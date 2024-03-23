# row check
def checkRow(row, player):
    for v in row:
        if v != player:
            return False
    return True

# col check
def checkCol(game, col, player):
    for row in game:
        if row[col] != player:
            return False
    return True

# check west diagonal
def westDiagonal(game, player):
    c = 0
    for row in game:
        if row[c] != player:
            return False
        c += 1
    return True 

# check east diagonal
def eastDiagonal(game, player):
    c = len(game) - 1
    for row in game:
        if row[c] != player:
            return False
        c -= 1
    return True 