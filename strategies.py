import math

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


def getCellsFromSameRow(puzzle, cellIndex):
    cells = []
    subjectRow = math.floor(cellIndex/9)
    subjectCol = cellIndex % 9
    for targetCellCol in range(0,9):
        if subjectCol == targetCellCol:
            # print('skipping index', targetCellCol)
            continue
        targetCellIndex = (9*subjectRow) + targetCellCol
        cells.append(puzzle[targetCellIndex])
    return cells

def getCellsFromSameColumn(puzzle, cellIndex):
    cells = []
    subjectRow = math.floor(cellIndex/9)
    subjectCol = cellIndex % 9
    for targetCellRow in range(0,9):
        if subjectRow == targetCellRow:
            continue
        targetCellIndex = (9*targetCellRow) + subjectCol
        cells.append(puzzle[targetCellIndex])
    return cells

def getCellsFromSameBlock(puzzle, cellIndex):
    'Top left block is 0, bottom right 8. Indexes for block 0 would be 0,1,2, 9,10,11, 18,19,20'
    cells = []
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
        cells.append(puzzle[targetIndex])
    print(f'Incoming index: {cellIndex}, incoming row: {subjectRow}, incoming cell: {subjectCol}')
    print(f'Block row: {blockRowNo}, Block col: {blockCellNo}, blockstart: {blockStartCell}')
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

