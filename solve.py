from renderer import renderPuzzleFromStarter, renderActivePuzzle
from examples import exampleStarter1, exampleStarter2, exampleStarter3, exampleStarter4
from utils import getPuzzleFromStarter
from strategies import (getCellsFromSameRow,
                        discountCellBasedOnCells,
                        getCellsFromSameColumn,
                        getCellsFromSameBlock,
                        solveSingleRemaindersByRow,
                        solveSingleRemaindersByCol
)
import json
import sys

def renderPuzzleAndWaitForInput(puzzle):
    renderActivePuzzle(puzzle)
    command = input(f'Pass {passCount}, Step{stepCount}')
    if command == 'save':
        f = open('quicksave.json', 'w')
        f.write(json.dumps(puzzle))
        f.close()
        print('saved quicksave.json')


if len(sys.argv) > 1 and sys.argv[1] == 'load':
    f = open('quicksave.json', 'r')
    puzzle = json.loads(f.read())
    f.close()
    renderActivePuzzle(puzzle)
    print('loaded from file')
else:
    puzzle = getPuzzleFromStarter(exampleStarter4)
    renderPuzzleFromStarter(exampleStarter4)
    

# print(puzzle[1])
input('Press enter to start solving')

# Begin a while loop that asks for prompt at the end of each step
# Each step aims to run through one iteration of a strategy
# There are a few strategies, starting with the cell-by-cell discount approach
passCount = 0
stepCount = 0
progressMadeSinceLastPrint = False

while True:
    passCount += 1
    # Keep track of whether progress has actually been made on this iteration.
    # If we get to the end and there's no progress, we're unable to solve.
    # Bail to avoid an infinite loop.
    progressMadeThisPass = False
    
    # Run the cell-by-cell strategy
    for cellIndex, cell in enumerate(puzzle):
        if puzzle[cellIndex]["solved"]:
            continue
        else:
            stepCount += 1
            # Discount values solved in the same row
            cells = getCellsFromSameRow(puzzle, cellIndex)
            print(f'row grabbed for index {cellIndex}', cells)
            updatedCell = discountCellBasedOnCells(cell, cells)
            if updatedCell:
                progressMadeThisPass = True
                progressMadeSinceLastPrint = True
                puzzle[cellIndex] = updatedCell
            
            # Discount values solved in the same column
            cells = getCellsFromSameColumn(puzzle, cellIndex)
            # print('cellIndexes grabbed', len(cells))
            updatedCell = discountCellBasedOnCells(cell, cells)
            if updatedCell:
                progressMadeThisPass = True
                progressMadeSinceLastPrint = True
                puzzle[cellIndex] = updatedCell
            
            # Discount values solved in the same black
            cells = getCellsFromSameBlock(puzzle, cellIndex)
            updatedCell = discountCellBasedOnCells(cell, cells)
            if updatedCell:
                progressMadeThisPass = True
                progressMadeSinceLastPrint = True
                puzzle[cellIndex] = updatedCell

        # renderActivePuzzle(puzzle)
        
        if progressMadeSinceLastPrint:
            progressMadeSinceLastPrint = False
            renderPuzzleAndWaitForInput(puzzle)

    # Next strategy: Is there only one place for X in each row?
    for rowIndex in range(0,9):
        stepCount += 1
        progressMade = solveSingleRemaindersByRow(puzzle, rowIndex)
        if progressMade:
            renderPuzzleAndWaitForInput(puzzle)
            progressMadeThisPass = True


    # Next strategy: Is there only one place for X in each col?
    for colIndex in range(0,9):
        stepCount += 1
        progressMade = solveSingleRemaindersByCol(puzzle, colIndex)
        if progressMade:
            renderPuzzleAndWaitForInput(puzzle)
            progressMadeThisPass = True

    # Next strategy: Is there only one place for X in each block? If 2-3 spots but in a line, rule out rest of line
    
    # Next strategy: checking for identical possibilities in one block and rule out rest of block

    # Next strategy: checking for identical possibilities in one row and rule out rest of row

    # Next strategy: checking for identical possibilities in one col and rule out rest of col

    # if by this point, no progress has been made, we can't solve the puzzle..!
    if not progressMadeThisPass:
        print('No progress made on this pass, could not solve!!!')
        break


    

    

