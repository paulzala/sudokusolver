from renderer import renderPuzzleFromStarter, renderActivePuzzle
from examples import exampleStarter1
from utils import getPuzzleFromStarter
from strategies import getCellsFromSameRow, discountCellBasedOnCells, getCellsFromSameColumn, getCellsFromSameBlock

renderPuzzleFromStarter(exampleStarter1)
puzzle = getPuzzleFromStarter(exampleStarter1)
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
            print('cellIndexes grabbed', len(cells))
            updatedCell = discountCellBasedOnCells(cell, cells)
            if updatedCell:
                progressMadeThisPass = True
                progressMadeSinceLastPrint = True
                puzzle[cellIndex] = updatedCell

        # TODO show progress here right before input - need to make the rendered first
        renderActivePuzzle(puzzle)
        
        if progressMadeSinceLastPrint:
            progressMadeSinceLastPrint = False
            input(f'Pass {passCount}, Step{stepCount}')

    # Next strategy: Is there only one place for X in each row?

    # Next strategy: Is there only one place for X in each col?

    # Next strategy: Is there only one place for X in each block? If 2-3 spots but in a line, rule out rest of line
    
    # Next strategy: checking for identical possibilities in one block and rule out rest of block

    # Next strategy: checking for identical possibilities in one row and rule out rest of row

    # Next strategy: checking for identical possibilities in one col and rule out rest of col

    # if by this point, no progress has been made, we can't solve the puzzle..!
    if not progressMadeThisPass:
        print('No progress made on this pass, could not solve!!!')
        break


    

    

