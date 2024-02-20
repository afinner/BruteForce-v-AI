import sys

class options:
    """
    Set tic-tac-toe runtime options
    """

    def __init__(self):
        self.x = "player"
        self.o = "ai"
        self.gridSize = 3
        self.games = 1
        self.display = "gui"
        self.switchO = -1
        self.aiDataFile = "agentData_" + str(self.gridSize) + ".pkl"
        args = sys.argv[1:]

        for i in range(0, len(args), 2):
            if args[i] == '-x':
                self.x = args[i+1]
            if args[i] == '-o':
                self.o = args[i+1]
            if args[i] == '-gridSize':
                self.gridSize = int(args[i+1])
                self.aiDataFile = "agentData_" + str(self.gridSize) + "_r5000.pkl"
            if args[i] == '-games':
                self.games = int(args[i+1])
            if args[i] == '-display':
                self.display = args[i+1]
            if args[i] == '-switchO':
                self.switchO = int(args[i+1])

        if self.x != "player" and self.display != "off":
            self.display = "text"

        if self.x == "player" and self.display == "off":
            self.display = "text"

        print(self.x, self.o, self.switchO, self.gridSize, self.games, self.display, self.aiDataFile )
