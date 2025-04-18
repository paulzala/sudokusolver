from strategies import (
    getCellsFromSameRow,
    discountCellBasedOnCells,
    getCellsFromSameColumn,
    getCellsFromSameBlock,
    cellCanBeMarkedSolved,
    solveSingleRemaindersByRow
)
from utils import getPuzzleFromStarter, unique
from renderer import renderActivePuzzle

readyToBeMarkedSolvedCell = {
    'solved': False,
    'discounts': {
        '1': True,
        '2': True,
        '3': True,
        '4': True,
        '5': False,
        '6': True,
        '7': True,
        '8': True,
        '9': True,
    }
}
result = cellCanBeMarkedSolved(readyToBeMarkedSolvedCell)
assert result == '5', result


cell = {
    'solved': False,
    'discounts': {
        '1': False,
        '2': False,
        '3': False,
        '4': False,
        '5': False,
        '6': False,
        '7': False,
        '8': False,
        '9': False,
    }
}
cellsForDiscountTest = [
    {'solved': '1'},
    {'solved': '2'},
    {'solved': '3'},
    {'solved': '4'},
    # no 5, test should solve it as 5
    {'solved': '6'},
    {'solved': '7'},
    {'solved': '8'},
    {'solved': '9'},
]
solvedCell = discountCellBasedOnCells(cell, cellsForDiscountTest)
assert solvedCell['solved'] == '5'

# Assert discount based on cell returns false if no progress
cell = {
    'solved': False,
    'discounts': {
        '1': False,
        '2': False,
        '3': False,
        '4': False,
        '5': False,
        '6': False,
        '7': False,
        '8': False,
        '9': False,
    }
}
result = discountCellBasedOnCells(cell, [{'solved': False}])
assert result == False, result


# assert that row-by-row single remainders can be solved. Will use a nonsense puzzle for the test
row0 = [
    # 1 can only go in cell 0, so should get solved as 1
    # 2 can go in 2 cells, so should not get solved
    # 3 can only go in last cell 8, so should get solved as 8 e
    # 5 is already solved in cell 4, so no other cells should be marked as solved 5
    {'solved': False, 'discounts': {'1': False, '2': False, '3': True,  '4': False, '5': False, '6': False, '7': False, '8': False, '9': False}},
    {'solved': False, 'discounts': {'1': True,  '2': True,  '3': True,  '4': False, '5': False, '6': False, '7': False, '8': False, '9': False}},
    {'solved': False, 'discounts': {'1': True,  '2': True,  '3': True,  '4': False, '5': False, '6': False, '7': False, '8': False, '9': False}},
    {'solved': False, 'discounts': {'1': True,  '2': False, '3': True,  '4': False, '5': False, '6': False, '7': False, '8': False, '9': False}},
    {'solved': '5',   'discounts': {'1': True,  '2': False, '3': True,  '4': False, '5': False, '6': False, '7': False, '8': False, '9': False}},
    {'solved': False, 'discounts': {'1': True,  '2': False, '3': True,  '4': False, '5': False, '6': False, '7': False, '8': False, '9': False}},
    {'solved': False, 'discounts': {'1': True,  '2': False, '3': True,  '4': False, '5': False, '6': False, '7': False, '8': False, '9': False}},
    {'solved': False, 'discounts': {'1': True,  '2': False, '3': True,  '4': False, '5': False, '6': False, '7': False, '8': False, '9': False}},
    {'solved': False, 'discounts': {'1': True,  '2': False, '3': False, '4': False, '5': False, '6': False, '7': False, '8': False, '9': False}},
]
# just duplicate the rows so method doesn't explode. we'll only check the cells of the first row
fullPuzzle = row0 * 9
result = solveSingleRemaindersByRow(fullPuzzle, 0)
assert(result == True)
# renderActivePuzzle(result)
assert(fullPuzzle[0]['solved'] == '1')
assert(fullPuzzle[4]['solved'] == '5')
assert(fullPuzzle[8]['solved'] == '3')
for index in range(0,9):
    assert(fullPuzzle[index]['solved'] != '2')


# assert unique function works
assert(len(unique([1,2,2,3])) == 3)

# assert gets correct cells
twoRows = list(range(0, 21))
result = getCellsFromSameRow(twoRows, 0)

# Should be 8 results, as itself won't be included
assert(len(result) == 8)
assert(result[0] == 1)
assert(result[7] == 8)

# Try one from middle of the second row
result = getCellsFromSameRow(twoRows, 12)

assert(len(result) == 8)
assert(result[0] == 9)
assert(result[7] == 17)

# Same tests for columns
puzzle = list(range(0, 81))
result = getCellsFromSameColumn(puzzle, 0)

# Should be 8 results, as itself won't be included
assert(len(result) == 8)
assert(result[0] == 9)
assert(result[7] == 72)

# Try one from middle of the fourth col
result = getCellsFromSameColumn(puzzle, 12)

assert(len(result) == 8)
assert(result[0] == 3)
assert(result[7] == 75)

# Same again for block
result = getCellsFromSameBlock(puzzle, 0)

# Should be 8 results, as itself won't be included
assert(len(result) == 8)
assert(result[0] == 1)
assert(result[7] == 20)

# Try one from middle of the second block at top
result = getCellsFromSameBlock(puzzle, 12)

assert(len(result) == 8)
assert(result[0] == 3)
assert(result[7] == 23)

