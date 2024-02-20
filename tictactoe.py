# Tic-tac-toe
import datetime
import time
import createGrid
import displayGrid
import userInput
import checkActive
import checkDraw
import compInput
import tableBaseData
#import tablebaseGenerator
import genericTb
import agent
import pickle
import os
import options
import psutil
import guiDisplay
import testPlayer
import randomCompMove

def main():
    opts = options.options()

    gridSize = opts.gridSize

    tablebase = []
    if opts.x == "bf" or opts.o == "bf" or (opts.switchO != -1):
        tablebase = tableBaseData.loadTablebase(gridSize)

    display = None
    if opts.display == "gui":
        display = guiDisplay.displayGrid(gridSize)
        
    if opts.o == "ai":
        ag = agent.initQAgent(opts)

    if opts.x or opts.o == "tester":
        tester = testPlayer.TestPlayer(0.9, gridSize)
    
    totalTime = 0
    totalCpuTime = 0
    winXCount = 0
    winOCount = 0

    psutil.cpu_percent(interval=None)

    stt = time.perf_counter_ns()

    for i in range(opts.games):
        game = createGrid.createGrid(gridSize)
        move = 0
        gameTime = 0
        gameCpuTime = 0
        gameIsActive = True

        if opts.switchO != -1:
            opts.o = "ai"

        row = -1
        col = -1
        while gameIsActive == True:
            reward = 0
            if opts.display == "text":
                displayGrid.displayOGrid(game)
            if opts.display == "gui":
                display.displayGrid(game, row, col)

            if (opts.switchO != -1) and move >= opts.switchO:
                opts.o = "bf"

            if move == 0:
                if opts.display == "text":
                    print('************ New Game *************')
                if opts.display == "gui":
                    display.draw_msg("New Game")

            # prompt user to input move
            if opts.x == "tester":
                row, col = tester.makeMove(game)
            elif opts.x == "player" and opts.display == "test":
                row, col = userInput.userInput(game, gridSize)
            elif opts.x == "player" and opts.display == "gui":
                gameIsActive, row, col = display.getMove()
                if gameIsActive == False:
                    continue
            elif opts.x == "bf":
                row, col = genericTb.getMove(game, tablebase)
            elif opts.x == "ai":
                row, col = ag.get_action(agent.getStateKey(game))
            elif opts.x == "random":
                row, col = randomCompMove.randomCompMove(game, gridSize)

            # Check the user move
            game[row][col] = 'X'
            won, line = checkActive.checkActive(game, gridSize, row, col)
            if won == True:
                gameIsActive = False
                reward = -1
                winXCount += 1
                if opts.display == "text":
                    print("Game is Over - you won")
                if opts.display == "gui":
                    display.displayWin(game,line)
                    display.draw_msg("Game Over - You Win")
                    time.sleep(3)
            elif checkDraw.checkDraw(game, gridSize) == True:
                gameIsActive = False
                if opts.display == "text":
                    print("Game is Over - Draw")
                if opts.display == "gui":
                    display.displayGrid(game, row, col)
                    display.draw_msg("Game Over - Draw")
                    time.sleep(3)

            # Update position
            if opts.display == "text":
                displayGrid.displayXGrid(game)
            if opts.display == "gui":
                display.displayGrid(game, row, col)
                time.sleep(1)

            move += 1

            if gameIsActive:
                
                # Request computer move
                st = time.perf_counter_ns()
                sct = time.process_time_ns()
                if opts.o == "basic":
                    row, col = compInput.compInput(game, gridSize)
                if opts.o == "bf":
                    row, col = genericTb.getMove(game, tablebase)
                if opts.o == "tester":
                    row, col = tester.makeMove(game)
                if opts.o == "ai":
                    row, col = ag.get_action(agent.getStateKey(game))
                gameTime += time.perf_counter_ns() - st
                gameCpuTime += time.process_time_ns() - sct

                # update Q-values
                if move > 1 and opts.o == "ai":
                    st = time.perf_counter_ns()
                    sct = time.process_time_ns()
                    ag.update(prevState, agent.getStateKey(game), prevMove, (row, col), 0)
                    gameTime += time.perf_counter_ns() - st
                    gameCpuTime += time.process_time_ns() - sct
                prevState = agent.getStateKey(game)
                prevMove = (row, col)

                # Check the computer move
                game[row][col] = 'O'
                won, line = checkActive.checkActive(game, gridSize, row, col)
                if won == True:
                    gameIsActive = False
                    reward = 1
                    winOCount += 1
                    if opts.display == "text":
                        print("Game is Over - you lost")
                        displayGrid.displayOGrid(game)
                    if opts.display == "gui":
                        display.displayWin(game,line)
                        display.draw_msg("Game Over - You Lose")
                        time.sleep(3)
                elif checkDraw.checkDraw(game, gridSize) == True:
                    gameIsActive = False
                    if opts.display == "text":
                        print("Game is Over - draw")
                        displayGrid.displayOGrid(game)
                    if opts.display == "gui":
                        display.displayGrid(game,row,col)
                        display.draw_msg("Game Over - Draw")
                        time.sleep(3)

                move += 1
                            
        if opts.o == "ai":
            st = time.perf_counter_ns()
            sct = time.process_time_ns()
            ag.update(prevState, None, prevMove, None, reward)
            gameTime += time.perf_counter_ns() - st
            gameCpuTime += time.process_time_ns() - sct
                
        totalTime += gameTime
        totalCpuTime += gameCpuTime

    trainingTime = time.perf_counter_ns() - stt

    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Total player-O time (us): ",end='')
    print(totalTime // 1000)
    print("Average player-O Time (us): ",end='')
    print(totalTime/opts.games // 1000)
    print("Total player-O CPU - time (us): ",end='')
    print(totalCpuTime // 1000)
    print("Average player-O CPU - Time (us): ",end='')
    print(totalCpuTime/opts.games // 1000)
    print("CPU percentage for run: ",end='')
    print(psutil.cpu_percent(interval=None))
    print("Games/Wins/Losses/Draws for player-O: ",end='')
    print(opts.games, winOCount, winXCount, opts.games - (winXCount+winOCount))
    print("Overall/Training time (ms): ",end='')
    print(trainingTime // 1000000)

    if opts.o == "ai" or (opts.switchO != -1):
        ag.save(opts.aiDataFile)

main()