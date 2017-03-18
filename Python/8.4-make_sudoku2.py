__author__ = 'minin'

import math
import random
import datetime

def init_field(size):
    # Initialize variables
    field, alphabet = [], []

    # Initialize field
    for pos_y in range(size**2):
        line = []

        for pos_x in range(size**2):
            line.append(0)
        field.append(line)

    # Initialize alphabet
    for num in range(1,len(field[0])+1):
        alphabet.append(num)

    # Return field and alphabet
    return field, alphabet

def check_position(pos_x, pos_y, field):

    # Check if position is empty
    if field[pos_x][pos_y] != 0:
        return 'Not zero'

    # Initialise alphabet
    alphabet = []
    for num in range(1,len(field[0])+1):
        alphabet.append(num)

    size = int(math.sqrt(len(alphabet)))

    # Delete numbers from the same line from the alphabet
    for x in range(size**2):
        try:
            alphabet.remove(field[x][pos_y])
        except ValueError:
            pass

    # Delete numbers from the same column from the alphabet
    for y in range(size**2):
        try:
            alphabet.remove(field[pos_x][y])
        except ValueError:
            pass

    # Delete numbers from the same quadrant from the alphabet
    quad_x_start = (pos_x / size) * size
    quad_x_finish = (pos_x / size) * size + size
    quad_y_start = (pos_y / size) * size
    quad_y_finish = (pos_y / size) * size + size

    for x in range(quad_x_start, quad_x_finish, 1):
        for y in range(quad_y_start, quad_y_finish, 1):
            try:
                alphabet.remove(field[x][y])
            except ValueError:
                pass

    # Return possible values
    if len(alphabet) == 0:
        return 'No possible values'
    else:
        return alphabet

def walk(cense, field):

    size = int(math.sqrt(len(field[0])))
    counter = 0

    for x in range(size**2):
            for y in range(size**2):
                if check_position(x, y, field) == 'No possible values':
                    #print 'Exit walk with position ' + str(x) + ' ' + str(y)
                    return size**2, field
                elif check_position(x, y, field) == 'Not zero':
                    counter += 1
                elif len(check_position(x, y, field)) == cense:
                    field[x][y] = random.sample(check_position(x, y, field), 1)[0]
                    #print str(field) + ' Added ' + str(field[x][y]) + ' to (' + str(x) + ', ' + str(y) +')'
                    return cense, field

    if counter == size**4:
        #print 'BINGO!'
        return 0, field
    else:
        #print 'Calling walk(' + str(cense + 1) + ', field)'
        return walk(cense + 1, field)

def walk_rand(field):

    size = int(math.sqrt(len(field[0])))

    x, y = random.randint(0, size**2 - 1), random.randint(0, size**2 - 1)
            #print x, y, field[x][y]

    while field[x][y] == 0:
        x, y = random.randint(0,size**2 - 1), random.randint(0,size**2 - 1)
        #print x, y, field[x][y]

    # Change value
    field[x][y] = 0
    field[x][y] = random.sample(check_position(x, y, field), 1)[0]
    #print str(field) + '(' + str(x) + ', ' + str(y) +') Changed to ' + str(field[x][y])
    return field

def make_sudoku(size):
    tmp = init_field(size)
    field = tmp[0]
    alphabet = tmp[1]

    field[0] = alphabet[:]
    random.shuffle(field[0])

    #print str(field) + ' Initial field'

    while True:

        tmp = walk(1,field)

        cense = tmp[0]
        field = tmp[1]

        #print field


        # Stop if all positions filled, otherwise start again
        if cense == 0:
            return field
        elif cense == size**2:
            field = walk_rand(field)
        else:
            pass


#for line in make_sudoku(3):
#    print line

for size in range(1,10):
    start = datetime.datetime.today()
    print '============= Times for size  ' + str(size) + ' ================'
    for i in range(5):
        make_sudoku(size)
        print datetime.datetime.today() - start
