def renderPuzzleFromStarter(puzzle):
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

# from examples import examplePuzzle1
# renderPuzzleFromStart(examplePuzzle1)

def renderActivePuzzle(puzzle):
    v = []
    for cell in puzzle:
        # print('cell', cell)
        if cell['solved']:
            v.append([' ',' ',' ',' ',cell['solved'],' ',' ',' ',' '])
        else:
            details = []
            for value in range(1,10):
                if cell['discounts'][str(value)]:
                    details.append('x')
                else:
                    details.append(' ')
            v.append(details)
    
    print(
    f'+=====+=====+=====+=====+=====+=====+=====+=====+=====+\n' +
    f'‖{v[0][0]} {v[0][1]} {v[0][2]}|{v[1][0]} {v[1][1]} {v[1][2]}|{v[2][0]} {v[2][1]} {v[2][2]}‖{v[3][0]} {v[3][1]} {v[3][2]}|{v[4][0]} {v[4][1]} {v[4][2]}|{v[5][0]} {v[5][1]} {v[5][2]}‖{v[6][0]} {v[6][1]} {v[6][2]}|{v[7][0]} {v[7][1]} {v[7][2]}|{v[8][0]} {v[8][1]} {v[8][2]}‖\n' +
    f'‖{v[0][3]} {v[0][4]} {v[0][5]}|{v[1][3]} {v[1][4]} {v[1][5]}|{v[2][3]} {v[2][4]} {v[2][5]}‖{v[3][3]} {v[3][4]} {v[3][5]}|{v[4][3]} {v[4][4]} {v[4][5]}|{v[5][3]} {v[5][4]} {v[5][5]}‖{v[6][3]} {v[6][4]} {v[6][5]}|{v[7][3]} {v[7][4]} {v[7][5]}|{v[8][3]} {v[8][4]} {v[8][5]}‖\n' +
    f'‖{v[0][6]} {v[0][7]} {v[0][8]}|{v[1][6]} {v[1][7]} {v[1][8]}|{v[2][6]} {v[2][7]} {v[2][8]}‖{v[3][6]} {v[3][7]} {v[3][8]}|{v[4][6]} {v[4][7]} {v[4][8]}|{v[5][6]} {v[5][7]} {v[5][8]}‖{v[6][6]} {v[6][7]} {v[6][8]}|{v[7][6]} {v[7][7]} {v[7][8]}|{v[8][6]} {v[8][7]} {v[8][8]}‖\n' +
    f'+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n' +
    f'‖{v[9][0]} {v[9][1]} {v[9][2]}|{v[10][0]} {v[10][1]} {v[10][2]}|{v[11][0]} {v[11][1]} {v[11][2]}‖{v[12][0]} {v[12][1]} {v[12][2]}|{v[13][0]} {v[13][1]} {v[13][2]}|{v[14][0]} {v[14][1]} {v[14][2]}‖{v[15][0]} {v[15][1]} {v[15][2]}|{v[16][0]} {v[16][1]} {v[16][2]}|{v[17][0]} {v[17][1]} {v[17][2]}‖\n' +
    f'‖{v[9][3]} {v[9][4]} {v[9][5]}|{v[10][3]} {v[10][4]} {v[10][5]}|{v[11][3]} {v[11][4]} {v[11][5]}‖{v[12][3]} {v[12][4]} {v[12][5]}|{v[13][3]} {v[13][4]} {v[13][5]}|{v[14][3]} {v[14][4]} {v[14][5]}‖{v[15][3]} {v[15][4]} {v[15][5]}|{v[16][3]} {v[16][4]} {v[16][5]}|{v[17][3]} {v[17][4]} {v[17][5]}‖\n' +
    f'‖{v[9][6]} {v[9][7]} {v[9][8]}|{v[10][6]} {v[10][7]} {v[10][8]}|{v[11][6]} {v[11][7]} {v[11][8]}‖{v[12][6]} {v[12][7]} {v[12][8]}|{v[13][6]} {v[13][7]} {v[13][8]}|{v[14][6]} {v[14][7]} {v[14][8]}‖{v[15][6]} {v[15][7]} {v[15][8]}|{v[16][6]} {v[16][7]} {v[16][8]}|{v[17][6]} {v[17][7]} {v[17][8]}‖\n' +
    f'+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n' +
    f'‖{v[18][0]} {v[18][1]} {v[18][2]}|{v[19][0]} {v[19][1]} {v[19][2]}|{v[20][0]} {v[20][1]} {v[20][2]}‖{v[21][0]} {v[21][1]} {v[21][2]}|{v[22][0]} {v[22][1]} {v[22][2]}|{v[23][0]} {v[23][1]} {v[23][2]}‖{v[24][0]} {v[24][1]} {v[24][2]}|{v[25][0]} {v[25][1]} {v[25][2]}|{v[26][0]} {v[26][1]} {v[26][2]}‖\n' +
    f'‖{v[18][3]} {v[18][4]} {v[18][5]}|{v[19][3]} {v[19][4]} {v[19][5]}|{v[20][3]} {v[20][4]} {v[20][5]}‖{v[21][3]} {v[21][4]} {v[21][5]}|{v[22][3]} {v[22][4]} {v[22][5]}|{v[23][3]} {v[23][4]} {v[23][5]}‖{v[24][3]} {v[24][4]} {v[24][5]}|{v[25][3]} {v[25][4]} {v[25][5]}|{v[26][3]} {v[26][4]} {v[26][5]}‖\n' +
    f'‖{v[18][6]} {v[18][7]} {v[18][8]}|{v[19][6]} {v[19][7]} {v[19][8]}|{v[20][6]} {v[20][7]} {v[20][8]}‖{v[21][6]} {v[21][7]} {v[21][8]}|{v[22][6]} {v[22][7]} {v[22][8]}|{v[23][6]} {v[23][7]} {v[23][8]}‖{v[24][6]} {v[24][7]} {v[24][8]}|{v[25][6]} {v[25][7]} {v[25][8]}|{v[26][6]} {v[26][7]} {v[26][8]}‖\n' +
    f'+=====+=====+=====+=====+=====+=====+=====+=====+=====+\n' +
    f'‖{v[27][0]} {v[27][1]} {v[27][2]}|{v[28][0]} {v[28][1]} {v[28][2]}|{v[29][0]} {v[29][1]} {v[29][2]}‖{v[30][0]} {v[30][1]} {v[30][2]}|{v[31][0]} {v[31][1]} {v[31][2]}|{v[32][0]} {v[32][1]} {v[32][2]}‖{v[33][0]} {v[33][1]} {v[33][2]}|{v[34][0]} {v[34][1]} {v[34][2]}|{v[35][0]} {v[35][1]} {v[35][2]}‖\n' +
    f'‖{v[27][3]} {v[27][4]} {v[27][5]}|{v[28][3]} {v[28][4]} {v[28][5]}|{v[29][3]} {v[29][4]} {v[29][5]}‖{v[30][3]} {v[30][4]} {v[30][5]}|{v[31][3]} {v[31][4]} {v[31][5]}|{v[32][3]} {v[32][4]} {v[32][5]}‖{v[33][3]} {v[33][4]} {v[33][5]}|{v[34][3]} {v[34][4]} {v[34][5]}|{v[35][3]} {v[35][4]} {v[35][5]}‖\n' +
    f'‖{v[27][6]} {v[27][7]} {v[27][8]}|{v[28][6]} {v[28][7]} {v[28][8]}|{v[29][6]} {v[29][7]} {v[29][8]}‖{v[30][6]} {v[30][7]} {v[30][8]}|{v[31][6]} {v[31][7]} {v[31][8]}|{v[32][6]} {v[32][7]} {v[32][8]}‖{v[33][6]} {v[33][7]} {v[33][8]}|{v[34][6]} {v[34][7]} {v[34][8]}|{v[35][6]} {v[35][7]} {v[35][8]}‖\n' +
    f'+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n' +
    f'‖{v[36][0]} {v[36][1]} {v[36][2]}|{v[37][0]} {v[37][1]} {v[37][2]}|{v[38][0]} {v[38][1]} {v[38][2]}‖{v[39][0]} {v[39][1]} {v[39][2]}|{v[40][0]} {v[40][1]} {v[40][2]}|{v[41][0]} {v[41][1]} {v[41][2]}‖{v[42][0]} {v[42][1]} {v[42][2]}|{v[43][0]} {v[43][1]} {v[43][2]}|{v[44][0]} {v[44][1]} {v[44][2]}‖\n' +
    f'‖{v[36][3]} {v[36][4]} {v[36][5]}|{v[37][3]} {v[37][4]} {v[37][5]}|{v[38][3]} {v[38][4]} {v[38][5]}‖{v[39][3]} {v[39][4]} {v[39][5]}|{v[40][3]} {v[40][4]} {v[40][5]}|{v[41][3]} {v[41][4]} {v[41][5]}‖{v[42][3]} {v[42][4]} {v[42][5]}|{v[43][3]} {v[43][4]} {v[43][5]}|{v[44][3]} {v[44][4]} {v[44][5]}‖\n' +
    f'‖{v[36][6]} {v[36][7]} {v[36][8]}|{v[37][6]} {v[37][7]} {v[37][8]}|{v[38][6]} {v[38][7]} {v[38][8]}‖{v[39][6]} {v[39][7]} {v[39][8]}|{v[40][6]} {v[40][7]} {v[40][8]}|{v[41][6]} {v[41][7]} {v[41][8]}‖{v[42][6]} {v[42][7]} {v[42][8]}|{v[43][6]} {v[43][7]} {v[43][8]}|{v[44][6]} {v[44][7]} {v[44][8]}‖\n' +
    f'+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n' +
    f'‖{v[45][0]} {v[45][1]} {v[45][2]}|{v[46][0]} {v[46][1]} {v[46][2]}|{v[47][0]} {v[47][1]} {v[47][2]}‖{v[48][0]} {v[48][1]} {v[48][2]}|{v[49][0]} {v[49][1]} {v[49][2]}|{v[50][0]} {v[50][1]} {v[50][2]}‖{v[51][0]} {v[51][1]} {v[51][2]}|{v[52][0]} {v[52][1]} {v[52][2]}|{v[53][0]} {v[53][1]} {v[53][2]}‖\n' +
    f'‖{v[45][3]} {v[45][4]} {v[45][5]}|{v[46][3]} {v[46][4]} {v[46][5]}|{v[47][3]} {v[47][4]} {v[47][5]}‖{v[48][3]} {v[48][4]} {v[48][5]}|{v[49][3]} {v[49][4]} {v[49][5]}|{v[50][3]} {v[50][4]} {v[50][5]}‖{v[51][3]} {v[51][4]} {v[51][5]}|{v[52][3]} {v[52][4]} {v[52][5]}|{v[53][3]} {v[53][4]} {v[53][5]}‖\n' +
    f'‖{v[45][6]} {v[45][7]} {v[45][8]}|{v[46][6]} {v[46][7]} {v[46][8]}|{v[47][6]} {v[47][7]} {v[47][8]}‖{v[48][6]} {v[48][7]} {v[48][8]}|{v[49][6]} {v[49][7]} {v[49][8]}|{v[50][6]} {v[50][7]} {v[50][8]}‖{v[51][6]} {v[51][7]} {v[51][8]}|{v[52][6]} {v[52][7]} {v[52][8]}|{v[53][6]} {v[53][7]} {v[53][8]}‖\n' +
    f'+=====+=====+=====+=====+=====+=====+=====+=====+=====+\n' +
    f'‖{v[54][0]} {v[54][1]} {v[54][2]}|{v[55][0]} {v[55][1]} {v[55][2]}|{v[56][0]} {v[56][1]} {v[56][2]}‖{v[57][0]} {v[57][1]} {v[57][2]}|{v[58][0]} {v[58][1]} {v[58][2]}|{v[59][0]} {v[59][1]} {v[59][2]}‖{v[60][0]} {v[60][1]} {v[60][2]}|{v[61][0]} {v[61][1]} {v[61][2]}|{v[62][0]} {v[62][1]} {v[62][2]}‖\n' +
    f'‖{v[54][3]} {v[54][4]} {v[54][5]}|{v[55][3]} {v[55][4]} {v[55][5]}|{v[56][3]} {v[56][4]} {v[56][5]}‖{v[57][3]} {v[57][4]} {v[57][5]}|{v[58][3]} {v[58][4]} {v[58][5]}|{v[59][3]} {v[59][4]} {v[59][5]}‖{v[60][3]} {v[60][4]} {v[60][5]}|{v[61][3]} {v[61][4]} {v[61][5]}|{v[62][3]} {v[62][4]} {v[62][5]}‖\n' +
    f'‖{v[54][6]} {v[54][7]} {v[54][8]}|{v[55][6]} {v[55][7]} {v[55][8]}|{v[56][6]} {v[56][7]} {v[56][8]}‖{v[57][6]} {v[57][7]} {v[57][8]}|{v[58][6]} {v[58][7]} {v[58][8]}|{v[59][6]} {v[59][7]} {v[59][8]}‖{v[60][6]} {v[60][7]} {v[60][8]}|{v[61][6]} {v[61][7]} {v[61][8]}|{v[62][6]} {v[62][7]} {v[62][8]}‖\n' +
    f'+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n' +
    f'‖{v[63][0]} {v[63][1]} {v[63][2]}|{v[64][0]} {v[64][1]} {v[64][2]}|{v[65][0]} {v[65][1]} {v[65][2]}‖{v[66][0]} {v[66][1]} {v[66][2]}|{v[67][0]} {v[67][1]} {v[67][2]}|{v[68][0]} {v[68][1]} {v[68][2]}‖{v[69][0]} {v[69][1]} {v[69][2]}|{v[70][0]} {v[70][1]} {v[70][2]}|{v[71][0]} {v[71][1]} {v[71][2]}‖\n' +
    f'‖{v[63][3]} {v[63][4]} {v[63][5]}|{v[64][3]} {v[64][4]} {v[64][5]}|{v[65][3]} {v[65][4]} {v[65][5]}‖{v[66][3]} {v[66][4]} {v[66][5]}|{v[67][3]} {v[67][4]} {v[67][5]}|{v[68][3]} {v[68][4]} {v[68][5]}‖{v[69][3]} {v[69][4]} {v[69][5]}|{v[70][3]} {v[70][4]} {v[70][5]}|{v[71][3]} {v[71][4]} {v[71][5]}‖\n' +
    f'‖{v[63][6]} {v[63][7]} {v[63][8]}|{v[64][6]} {v[64][7]} {v[64][8]}|{v[65][6]} {v[65][7]} {v[65][8]}‖{v[66][6]} {v[66][7]} {v[66][8]}|{v[67][6]} {v[67][7]} {v[67][8]}|{v[68][6]} {v[68][7]} {v[68][8]}‖{v[69][6]} {v[69][7]} {v[69][8]}|{v[70][6]} {v[70][7]} {v[70][8]}|{v[71][6]} {v[71][7]} {v[71][8]}‖\n' +
    f'+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n' +
    f'‖{v[72][0]} {v[72][1]} {v[72][2]}|{v[73][0]} {v[73][1]} {v[73][2]}|{v[74][0]} {v[74][1]} {v[74][2]}‖{v[75][0]} {v[75][1]} {v[75][2]}|{v[76][0]} {v[76][1]} {v[76][2]}|{v[77][0]} {v[77][1]} {v[77][2]}‖{v[78][0]} {v[78][1]} {v[78][2]}|{v[79][0]} {v[79][1]} {v[79][2]}|{v[80][0]} {v[80][1]} {v[80][2]}‖\n' +
    f'‖{v[72][3]} {v[72][4]} {v[72][5]}|{v[73][3]} {v[73][4]} {v[73][5]}|{v[74][3]} {v[74][4]} {v[74][5]}‖{v[75][3]} {v[75][4]} {v[75][5]}|{v[76][3]} {v[76][4]} {v[76][5]}|{v[77][3]} {v[77][4]} {v[77][5]}‖{v[78][3]} {v[78][4]} {v[78][5]}|{v[79][3]} {v[79][4]} {v[79][5]}|{v[80][3]} {v[80][4]} {v[80][5]}‖\n' +
    f'‖{v[72][6]} {v[72][7]} {v[72][8]}|{v[73][6]} {v[73][7]} {v[73][8]}|{v[74][6]} {v[74][7]} {v[74][8]}‖{v[75][6]} {v[75][7]} {v[75][8]}|{v[76][6]} {v[76][7]} {v[76][8]}|{v[77][6]} {v[77][7]} {v[77][8]}‖{v[78][6]} {v[78][7]} {v[78][8]}|{v[79][6]} {v[79][7]} {v[79][8]}|{v[80][6]} {v[80][7]} {v[80][8]}‖\n' +
    f'+=====+=====+=====+=====+=====+=====+=====+=====+=====+')

