import generateOptions
import genericTb

def main():
    opts = generateOptions.generateOptions()
    genericTb.bruteforceGame(opts.gridsize, opts.tablebaseCount)

main()
