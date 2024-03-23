import sys

class generateOptions:
    """
    Set generate tablebase runtime options
    """

    def __init__(self):
        self.gridsize = 3
        self.tablebaseCount = 10
        args = sys.argv[1:]

        for i in range(0, len(args), 2):
            if args[i] == '-g':
                self.gridsize = int(args[i+1])
            if args[i] == '-t':
                self.tablebaseCount = int(args[i+1])

        if self.tablebaseCount > (self.gridsize*self.gridsize)+1:
            self.tablebaseCount = (self.gridsize*self.gridsize)+1
        if self.tablebaseCount <= 2:
            self.tablebaseCount = 3

        print(self.gridsize, self.tablebaseCount)
