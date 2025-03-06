from strategies import getCellsFromSameRow, discountCellBasedOnCells, getCellsFromSameColumn, cellCanBeMarkedSolved

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