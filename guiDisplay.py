# Tic-Tac-Toe Game with Python
import pygame
import sys

class displayGrid:
    WINDOW_SIZE = 720
    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    LINE_COLOR = (0, 0, 0)
    HIGH_COLOR = (255, 0, 0)

    def __init__(self, gridSize=3):
        self.running = True
        self.game_over = False
        self.gridSize = gridSize

        # Initialize Pygame
        pygame.init()
        self.game_font = pygame.freetype.SysFont("courrier", 38) #arial, #courrier ?

        # Constants
        self.GRID_SIZE = displayGrid.WINDOW_SIZE // self.gridSize
        self.LINE_WIDTH = 10

        # Set up the display
        self.screen = pygame.display.set_mode((displayGrid.WINDOW_SIZE, displayGrid.WINDOW_SIZE))
        pygame.display.set_caption('Tic Tac Toe')

    def draw_lines(self):
        for i in range(1, self.gridSize):
            pygame.draw.line(self.screen, displayGrid.LINE_COLOR, (i * self.GRID_SIZE, 0), (i * self.GRID_SIZE, self.WINDOW_SIZE), self.LINE_WIDTH)
            pygame.draw.line(self.screen, self.LINE_COLOR, (0, i * self.GRID_SIZE), (self.WINDOW_SIZE, i * self.GRID_SIZE), self.LINE_WIDTH)

    def draw_x(self, row, col, color=None):
        if color == None:
            color=displayGrid.LINE_COLOR
        offset = self.GRID_SIZE // 4
        pygame.draw.line(self.screen, color, (col * self.GRID_SIZE + offset, row * self.GRID_SIZE + offset),
                        ((col + 1) * self.GRID_SIZE - offset, (row + 1) * self.GRID_SIZE - offset), self.LINE_WIDTH)
        pygame.draw.line(self.screen, color, ((col + 1) * self.GRID_SIZE - offset, row * self.GRID_SIZE + offset),
                        (col * self.GRID_SIZE + offset, (row + 1) * self.GRID_SIZE - offset), self.LINE_WIDTH)

    def draw_o(self, row, col, color=None):
        if color == None:
            color=displayGrid.LINE_COLOR
        offset = self.GRID_SIZE // 4
        pygame.draw.circle(self.screen, color, (col * self.GRID_SIZE + self.GRID_SIZE // 2, row * self.GRID_SIZE + self.GRID_SIZE // 2),
                        self.GRID_SIZE // 2 - offset, self.LINE_WIDTH)

    def draw_msg(self, message):
        font = pygame.font.SysFont(None, 60)
        text = font.render(message, True, displayGrid.HIGH_COLOR, (0,0,0))
        self.screen.blit(text, text.get_rect(center = self.screen.get_rect().center))
        pygame.display.flip()

    def displayGrid(self, game, row=-1, col=-1):
        self.screen.fill(self.WHITE)
        self.draw_lines()
        for r in range(self.gridSize):
            for c in range(self.gridSize):
                color = self.LINE_COLOR
                if r == row and c == col:
                    color = self.HIGH_COLOR
                if game[r][c] == 'X': 
                    self.draw_x(r, c, color)
                elif game[r][c]  == 'O':
                    self.draw_o(r, c, color)
        pygame.display.flip()

    def getMove(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return False, -1, -1

                if not self.game_over and event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row, col = y // self.GRID_SIZE, x // self.GRID_SIZE
                    return True, row, col

    def displayWin(self, game, line):
        self.screen.fill(self.WHITE)
        self.draw_lines()
        for r in range(self.gridSize):
            for c in range(self.gridSize):
                color = self.LINE_COLOR
                for i in range(len(line)):
                    if line[i] == (r, c):
                        color = self.HIGH_COLOR
                        break
                if game[r][c] == 'X': 
                    self.draw_x(r, c, color)
                elif game[r][c]  == 'O':
                    self.draw_o(r, c, color)
        pygame.display.flip()

    def close():
        pygame.quit()
        sys.exit()


def main():
    # Main game loop

    display = displayGrid(4)

    current_player = 'X'
    game = [['_','_','_','_'],['_','_','_','_'],['_','_','_','_'],['_','_','_','_']]

    display.displayGrid(game)
    display.draw_msg("New Game")
    while display.running:
        moved, r, c = display.getMove()
        if moved:
            game[r][c] = current_player
            current_player = 'O' if current_player == 'X' else 'X'
            display.displayGrid(game, r, c)
            if( r==3 and c==3 ):
                display.displayWin(game, [(0,0),(1,1),(2,2),(3,3)])
                display.draw_msg("A player Wins")

    display.close()

#main()