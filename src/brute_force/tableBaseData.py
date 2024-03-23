
def outputData(tablebase, numBlanks, gridSize):
    maxBlanks = gridSize*gridSize
    file = open("Tablebase" + str(maxBlanks-numBlanks) + ".csv", "a")
    file.seek(0)
    file.truncate()
    for k,v in tablebase.items():
        file.write(str(k) + ",")
        file.write(str(v[0]) + ",")
        file.write(str(v[1]) + ",")
        file.write(str(v[2]) + ",")
        file.write(str(v[3]) + "\n")
    file.close()

def inputData(tablebase, numBlanks, gridSize):
    maxBlanks = gridSize*gridSize
    file = open("Tablebase" + str(maxBlanks-numBlanks) + ".csv", "r")
    for line in file.readlines():
        items = line.rstrip("\n").split(",")
        if len(items) != 5:
            print("Error, line items len != 5: " + line)
            continue
        tablebase[int(items[0])] = (int(items[1]), float(items[2]), int(items[3]), int(items[4]))

def loadTablebase(gridSize):
    tablebase = []
    for i in range (0, (gridSize*gridSize) + 1, 1):
        tablebase.append({})
    for numBlanks in range(0, gridSize*gridSize +1, 1):
        inputData(tablebase[numBlanks], numBlanks, gridSize)
    return tablebase

def main():
    tablebase = {}
    tablebase[1000] = (1,1,0,0)
    outputData(tablebase, numBlanks=0, gridSize=3)
    tablebaseX = {}
    inputData(tablebaseX, numBlanks=0, gridSize=3)
    print(tablebaseX)
    outputData(tablebaseX, numBlanks=0, gridSize=3)

#main()
