# AIvBF: N-Dimensional Tic-Tac-Toe Game Engine Comparison
The **AIvBF** repository is dedicated to implementing and measuring the performance of two game engines: a **Q-learning AI** and a **Brute Force** algorithm in the context of N-dimensional tic-tac-toe. This project allows you to explore and compare the strategies employed by these two engines.

## Features
### Q-learning AI:
Train the AI by playing games against it.
Utilize the training algorithm to improve the AI’s performance.
Observe how the AI adapts its strategy over time.
### Brute Force Algorithm:
Generate brute force tablebases for different grid sizes.
Understand the optimal moves for each possible game state.
Compare the efficiency of brute force versus learned strategies.
### Engine vs. Engine:
Pitch both game engines against each other:
AI vs. Brute Force
AI vs. Random Move Engine
Brute Force vs. Random Move Engine
AI vs. AI (self-play)
Analyze the initial cost and the cost of each iteration for different scenarios.
# Code Structure
The source files are organized within the [src] folder, which contains three sub-folders:

### game.py:
Implements the core game logic for N-dimensional tic-tac-toe.
Handles board state, moves, and win conditions.
### bruteForce.py:
Contains code related to the brute force algorithm.
Generates lookup tables for different grid sizes.
Provides optimal moves based on precomputed data.
### AI.py:
Houses the Q-learning AI implementation.
Includes training algorithms and decision-making logic.
The Brute Force folder specifically focuses on creating lookup tables for various grid sizes.

# Running the Program
To initialize the game loop, use the following command:

``python tictactoe.py -gridSize (3/4/5) -x (ai/player/tester) -o (ai/bf) -switchO (0-gridsize) -display gui -games 1``

Replace the placeholders with appropriate values:

-gridSize: Specify the grid size (3, 4, or 5).
-x: Choose the player type for X (AI, player, or tester).
-o: Choose the player type for O (AI or brute force).
-switchO: Set the switch position for O (0 to grid size).
-display: Select the display mode (e.g., “gui” for graphical interface).
-games: Specify the number of games to play.
Feel free to explore, experiment, and compare the performance of these game engines!
