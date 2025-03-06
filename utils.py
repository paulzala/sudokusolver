def getPuzzleFromStarter(starter):
    'Takes a starter puzzle list and converts to a Puzzle with solved/discounts state'
    # Each puzzle is an array of 81 objects. Each object contains a solved (int/false) and a discounts (object) key.
    # Each discounts object contains string keys from '1'-'9', with a true or false in them.
    # If solved, the discounts should all be marked true (except for the solved number of course)
    puzzle = []
    if len(starter) != 9:
        raise ValueError('Incorrect format')
    for line in starter:
        if len(line) != 9:
            raise ValueError('Incorrect format')
        for cellValue in line:
            cell = {}
            if cellValue in {' ', '0'}:
                # cell is unsolved
                cell['solved'] = False
                cell['discounts'] = {
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
            else:
                cell['solved'] = cellValue
                cell['discounts'] = {
                    '1': True,
                    '2': True,
                    '3': True,
                    '4': True,
                    '5': True,
                    '6': True,
                    '7': True,
                    '8': True,
                    '9': True,
                }
                cell['discounts'][cellValue] = True
            puzzle.append(cell)
    return puzzle

