import math
from utils import unique

# below might not be necessary
def checkCellAgainstOwnRow(puzzle, cellIndex, progressMade):
    # get the row and col position of the cell being checked, ie top left is 0,0
    subjectRow = math.floor(cellIndex/9)
    subjectCol = cellIndex % 9
    for testCellCol in range(0,9):
        if subjectCol == testCellCol:
            # print('skipping index', testCellCol)
            continue
        testCellIndex = (9*subjectRow) + testCellCol
        # print('testing against cell index', testCellIndex)
        testCell = puzzle[testCellIndex]
        # print('testCell', testCell)
        if (testCell["solved"]):
            solvedValue = testCell["solved"]
            if (not puzzle[cellIndex]['discounts'][solvedValue]):
                # i don't know if this affects the outside variable, need to check
                progressMade = True
                puzzle[cellIndex]['discounts'][solvedValue] = True


def getCellIndexesFromSameRow(cellIndex):
    resultIndexes = []
    subjectRow = math.floor(cellIndex/9)
    subjectCol = cellIndex % 9
    for targetCellCol in range(0,9):
        if subjectCol == targetCellCol:
            continue
        targetCellIndex = (9*subjectRow) + targetCellCol
        resultIndexes.append(targetCellIndex)
    return resultIndexes

def getCellsFromSameRow(puzzle, cellIndex):
    cells = []
    for targetCellIndex in getCellIndexesFromSameRow(cellIndex):
        cells.append(puzzle[targetCellIndex])
    return cells

def getCellIndexesFromSameColumn(cellIndex):
    resultIndexes = []
    subjectRow = math.floor(cellIndex/9)
    subjectCol = cellIndex % 9
    for targetCellRow in range(0,9):
        if subjectRow == targetCellRow:
            continue
        targetCellIndex = (9*targetCellRow) + subjectCol
        resultIndexes.append(targetCellIndex)
    return resultIndexes

def getCellsFromSameColumn(puzzle, cellIndex):
    cells = []
    for targetCellIndex in getCellIndexesFromSameColumn(cellIndex):
        cells.append(puzzle[targetCellIndex])
    return cells

def getCellIndexesFromSameBlock(cellIndex):
    'Top left block is 0, bottom right 8. Indexes for block 0 would be 0,1,2, 9,10,11, 18,19,20'
    resultIndexes = []
    # get the co-ordinates of the target cell
    subjectRow = math.floor(cellIndex/9)
    subjectCol = cellIndex % 9
    # round to the top-left co-ords of the block
    blockRowNo = (math.floor(subjectRow/3))*3
    blockCellNo = (math.floor(subjectCol/3))*3
    blockStartCell = (9*blockRowNo) + blockCellNo
    
    for offsetIndex in [0,1,2,9,10,11,18,19,20]:
        targetIndex = blockStartCell + offsetIndex
        if cellIndex == targetIndex:
            continue
        resultIndexes.append(targetIndex)
    return resultIndexes

def getCellsFromSameBlock(puzzle, cellIndex):
    cells = []
    for targetIndex in getCellIndexesFromSameBlock(cellIndex):
        cells.append(puzzle[targetIndex])
    return cells


def discountCellBasedOnCells(cell, cells):
    isChanged = False
    for testCell in cells:
        if (testCell["solved"]):
            solvedValue = testCell["solved"]
            if (not cell['discounts'][solvedValue]):
                isChanged = True
                cell['discounts'][solvedValue] = True
    # While we're here, check if the cell is solved
    if (isChanged):
        solvedValue = cellCanBeMarkedSolved(cell)
        if (solvedValue):
            cell = markCellSolved(cell, solvedValue)
    
    return cell if isChanged else False

def cellCanBeMarkedSolved(cell):
    'Either returns False, or the value that the cell can be marked solved as'
    firstPossibleValue = False
    for value in range(1,10):
        value = str(value)
        if (not cell['discounts'][value]):
            if not firstPossibleValue:
                firstPossibleValue = value
            else:
                return False
    return firstPossibleValue


def markCellSolved(cell, solvedValue):
    for value in range(1,10):
        value = str(value)
        if value == solvedValue:
            cell['solved'] = solvedValue
        else:
            cell['discounts'][value] = False
    return cell

def solveSingleRemaindersByRow(puzzle, rowIndex):
    'Takes a puzzle and a row, then value by value, looks for if a cell is the only place left for it'
    isChanged = False
    
    for value in range(1,10):
        value = str(value)
        valueWasFoundInColumn = None
        for colIndex in range(0,9):
            cell = puzzle[(rowIndex * 9) + colIndex]
            # if the cell is already solved and its actually the value we're checking against,
            # move to the next value and start next row from the beginning
            if cell['solved'] == value:
                # print(f'nevermind, {value} is solved on this row')
                valueWasFoundInColumn = None
                break
            # otherwise if it's solved but some other value, keep moving to the next cell
            elif cell['solved']:
                continue

            # If this cell could be the value, mark it. If we've already marked the possibility in this row,
            # then we can't solve this value yet.
            if not cell['discounts'][value]:
                if valueWasFoundInColumn == None:
                    # print(f'\'{value}\' can go in cell {(rowIndex * 9) + colIndex}')
                    valueWasFoundInColumn = colIndex
                else:
                    valueWasFoundInColumn = None
                    # print(f'\'{value}\' can also go in cell {(rowIndex * 9) + colIndex} so no luck')
                    break
            
        # If it has made it this far and exactly one value has been found, we have a winner!
        if valueWasFoundInColumn != None:
            isChanged = True
            cellIndex = (rowIndex * 9) + valueWasFoundInColumn
            # print(f'marking cell {cellIndex} as solve= \'{value}\'')
            puzzle[cellIndex] = markCellSolved(puzzle[cellIndex], value)
            # since we've solved things, we also need to check any affected cells in row/col/block and discount this value before moving on
            processDiscountsAfterIndexSolved(puzzle, cellIndex, value)
        # Either way, continue to the next value
    # End of the row, will Continue to the next row outside function
    return isChanged

def solveSingleRemaindersByCol(puzzle, colIndex):
    'Takes a puzzle and a col, then value by value, looks for if a cell is the only place left for it'
    isChanged = False
    
    for value in range(1,10):
        value = str(value)
        valueWasFoundInRow = None
        for rowIndex in range(0,9):
            cell = puzzle[(rowIndex * 9) + colIndex]
            # if the cell is already solved and its actually the value we're checking against,
            # move to the next value and start next col from the beginning
            if cell['solved'] == value:
                # print(f'nevermind, {value} is solved on this col')
                valueWasFoundInRow = None
                break
            # otherwise if it's solved but some other value, keep moving to the next cell
            elif cell['solved']:
                continue

            # If this cell could be the value, mark it. If we've already marked the possibility in this col,
            # then we can't solve this value yet.
            if not cell['discounts'][value]:
                if valueWasFoundInRow == None:
                    print(f'\'{value}\' can go in cell {(rowIndex * 9) + colIndex}')
                    valueWasFoundInRow = rowIndex
                else:
                    valueWasFoundInRow = None
                    print(f'\'{value}\' can also go in cell {(rowIndex * 9) + colIndex} so no luck')
                    break
            
        # If it has made it this far and exactly one value has been found, we have a winner!
        if valueWasFoundInRow != None:
            isChanged = True
            cellIndex = (valueWasFoundInRow * 9) + colIndex
            # print(f'marking cell {cellIndex} as solve= \'{value}\'')
            puzzle[cellIndex] = markCellSolved(puzzle[cellIndex], value)
            # since we've solved things, we also need to check any affected cells in row/col/block and discount this value before moving on
            processDiscountsAfterIndexSolved(puzzle, cellIndex, value)
        # Either way, continue to the next value
    # End of the col, will Continue to the next col outside function
    return isChanged

def processDiscountsAfterIndexSolved(puzzle, solvedIndex, value):
    'After cell index has been solved, add the discount value to affected cells, same row, col or block'
    print(f'index {solvedIndex} being marked {value}')
    checkIndexes = unique(getCellIndexesFromSameRow(solvedIndex) + getCellIndexesFromSameColumn(solvedIndex) + getCellIndexesFromSameRow(solvedIndex))
    for checkIndex in checkIndexes:
        cell = puzzle[checkIndex]
        if not cell['solved'] and not cell['discounts'][value]:
            cell['discounts'][value] = True
            solvedValue = cellCanBeMarkedSolved(cell)
            if solvedValue:
                print(f'cell {checkIndex} being marked solved after rowbyrow')
                markCellSolved(cell, solvedValue)
                processDiscountsAfterIndexSolved(puzzle, checkIndex, solvedValue)

