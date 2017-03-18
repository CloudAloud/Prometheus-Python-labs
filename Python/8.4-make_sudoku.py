__author__ = 'minin'

import random

def premake_sudoku(size):

    # Initialize variables
    result, alphabet = [], []

    # Initialize alphabet
    for i in range(1,size**2+1):
        alphabet.append(i)


    # Initialize result size
    for pos_y in range(size**2):
        line = []

        for pos_x in range(size**2):
            line.append(0)
        result.append(line)


    # Initialize first line
    result[0] = alphabet[:]
    random.shuffle(result[0])

    #
    for pos_y in range(1, size**2):

        for pos_x in range(size**2):

            new_alphabet = alphabet[:]
            local_pos_x = pos_x - 1
            local_pos_y = pos_y - 1

            # Delete numbers from the same line from new_alphabet
            while local_pos_x >= 0:
                #print pos_y, local_pos_x
                new_alphabet.remove(result[pos_y][local_pos_x])
                local_pos_x -= 1
            #print alphabet, new_alphabet, result[local_pos_y], result[pos_y]
            local_pos_x = pos_x - 1

            # Delete numbers from the same column from new_alphabet
            while local_pos_y >= 0:
                try:
                    new_alphabet.remove(result[local_pos_y][pos_x])
                except ValueError:
                    pass
                local_pos_y -= 1

            # Delete numbers from the same quadrant from new_alphabet

            for quad_y in range((pos_y / size) * size, (pos_y / size) * size + size, 1):
                for quad_x in range((pos_x / size) * size, (pos_x / size) * size + size, 1):
                    #print pos_y, pos_x, quad_y, quad_x
                    if (quad_y < pos_y):
                        try:
                            new_alphabet.remove(result[quad_y][quad_x])
                        except ValueError:
                            pass
                    elif (quad_x < pos_x):
                        try:
                            new_alphabet.remove(result[quad_y][quad_x])
                        except ValueError:
                            pass


                    #print pos_y, pos_x, quad_y, quad_x


            # Fill next value or start again if not possible
            try:
                result[pos_y][pos_x] = random.sample(new_alphabet, 1)[0]
            except ValueError:
                #return result
                return False
                #return premake_sudoku(size)

    return result

def make_sudoku(size):

    result = False
    counter = 0
    while result == False:
        result = premake_sudoku(size)
        counter += 1
        if counter % 1000 == 0:
            print counter
    print counter
    return result

for line in make_sudoku(4)[:]:
    print line
