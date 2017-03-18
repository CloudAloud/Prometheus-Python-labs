__author__ = 'minin'

def make_sudoku(size):

    field = []
    for j in range(size):
        for n in range(size):
            line = []
            for i in range(size**2):
                line.append((i + j + n * size) % (size**2) + 1)
            field.append(line)
    return field

make_sudoku(42)
