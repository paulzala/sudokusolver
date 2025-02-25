def renderPuzzleFromStart(puzzle):
    'Send in a sample puzzle, list of 9-character strings, and it will render to console.'
    for i, c in enumerate(puzzle):
        c = c.replace('0', ' ')
        if (i % 3 == 0):
            print((9 * '+=====') + '+')
        else:
            print((9 * '+-----') + '+')
        
        print((3 * '‖     |     |     ') + '‖')
        print(
            f'‖  {c[0]}  |  {c[1]}  |  {c[2]}  ' +
            f'‖  {c[3]}  |  {c[4]}  |  {c[5]}  ' +
            f'‖  {c[6]}  |  {c[7]}  |  {c[8]}  ‖'
        )
        print((3 * '‖     |     |     ') + '‖')
    
    print((9 * '+=====') + '+')

from examples import examplePuzzle1
renderPuzzleFromStart(examplePuzzle1)

