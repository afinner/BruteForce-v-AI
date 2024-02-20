# Tic-tac-toe
def displayXGrid(game):
    print('')
    for row in game:
       print(*row, sep=' | ', end='\n')
    
def displayOGrid(game):    
    print('')
    for row in game:
       print(' '*len(game),end='')
       print(*row, sep=' | ', end='\n')
    #    for v in row:
    #     print('    '+v+' | ', end='\n')
