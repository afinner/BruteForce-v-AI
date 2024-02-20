# AIvBF
This is a repository for implementing and measuring the cost of two game engines a qlearining AI and a brute force algorithm in a game of N-dimensional tic-tac-toe.
A user can train the AI (by playing games against it, or using the training algorithm), generate the brute force tablebases, pitch both game engines against a game engine making a random move or against themselves, and compare their initial cost and the cost of each iteration. 
# Code structure
There are 20 source files which contain elements of the AI, Brute Force or main game arena.
# Running the program
To initilize the game loop:
tictactoe.py -gridSize (3/4/5) -x (ai/player/tester) -o (ai/bf) -switchO (0-gridsize) -display gui -games 1
