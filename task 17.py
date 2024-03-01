def check_color(cell):
    letters = 'abcdefgh'
    row, col = cell[0], int(cell[1])

    if (letters.index(row)+1 + col)&1 == 0:
        return 'black'
    return 'white'

from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ['col\Row', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

def out_space():
    letters = 'abcdefgh'
    
    space = []

    for column in range(0,8):
        space.append([1,2,3,4,5,6,7,8])
        for letter in letters:
            let_ind = letters.index(letter)
            cell = letter+str(column+1)
            space[column][let_ind] = f'{letter}{column+1}({let_ind+column+2}{check_color(cell)})'
    
    for i, row in enumerate(space[::-1], 1):
        table.add_row([f'{9-i}', *row])

    print(table)
