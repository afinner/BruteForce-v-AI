# AIvBF: N-Dimensional Tic-Tac-Toe Game Engine Comparison
The **AIvBF** repository is dedicated to implementing and measuring the performance of two game engines: a **Q-learning AI** and a **Brute Force** algorithm in the context of N-dimensional tic-tac-toe. This project allows you to explore and compare the strategies employed by these two engines.

## Features
1. Q-learning AI:
   - Train the AI by playing games against it.
   - Utilize the training algorithm to improve the AI’s performance.
   - Observe how the AI adapts its strategy over time.
2. Brute Force Algorithm:
   - Generate brute force tablebases for different grid sizes.
   - Understand the optimal moves for each possible game state.
   - Compare the efficiency of brute force versus learned strategies.
3. Engine vs. Engine:
   - Pitch both game engines against each other:
     - AI vs. Brute Force
     - AI vs. Random Move Engine
     - Brute Force vs. Random Move Engine
     - AI vs. AI
   - Analyze the initial cost, and the cost of each iteration for different scenarios.
4. Project Report Book:
   - I've also included my project report book from the competition [here]()
# Code Structure
The source files are organized within the ``src`` folder, which contains two files:
1. ``tictactoe.py`` (which can be called to run the game)
2. ``genericTb.py`` (which can be called to generate tablebases of different grid sizes)

It also contains three sub-folders:

1. game.py:
   - Implements the core game logic for N-dimensional tic-tac-toe.
   - Handles board state, moves, and win conditions.
2. bruteForce.py:
   - Contains code related to the brute force algorithm.
   - Generates lookup tables for different grid sizes.
   - Provides optimal moves based on precomputed data.
3. AI.py:
   - Houses the Q-learning AI implementation.
   - Includes training algorithms and decision-making logic.
   - The code for the AI was adapted from [an opensource gitHub repository](https://github.com/rfeinman/tictactoe-reinforcement-learning/tree/master/tictactoe)

# Running the Program
### To initialize the game loop, use the following command:

``py -3.11 tictactoe.py``

Type in the following commands afterwards to explore different options:

``-gridSize (3/4/5) -x (ai/player/tester) -o (ai/bf) -switchO (0-gridsize) -display gui -games 1``

Replace the placeholders with appropriate values (otherwise it will automatically go with the defaut parameters):

1. ``-x``: Choose the player type for X ("ai", "player", or "tester").
2. ``-o``: Choose the player type for O ("ai" or "bf").
3. ``-gridSize``: Specify the grid size (either 3 or 4 if you want to use the Brute Force algorithm).
4. ``-games``: Specify the number of games to play.
5. ``-display``: Select the display mode ("gui","text" or "off").
6. ``-switchO``: Set the switch position for O, used when combining AI and Brute Force game engines (0 to size of grid squared).
7. ``-aiDataFile``: Specify where to store data from AI

### To initialize the generation of tablebases, use the following command:

``py -3.11 generateTablebase.py``

Type in the following commands afterwards to explore different options:

``-g (3/4) -t (1 to size of grid squared plus one)``

Replace the placeholders with appropriate values:

1. ``-g``: Specify the grid size (either 3 or 4)
2. ``-t``: Specify the number of tablebases you want to generate. (It will generate the tablebase with the greatest number of pieces first (i.e grid sizer squared) and decrement by one piece for each tablebase after that) (1 to size of grid squared plus one)

### Using Visual Studio Code:

I used the IDE VSCode throughout the design and implementation so I would advice using this IDE as I have not check compatiability with other IDEs, however you can also run from command line.   
Feel free to explore, experiment, and compare the performance of these game engines!
