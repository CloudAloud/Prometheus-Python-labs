__author__ = 'minin'


from final_maze_runner import *

class robot:

    def __init__(self, mr):
        self.direction = 'South'
        self.x = 0
        self.y = 0
        #self.position = [self.x, self.y]
        self.maze_map = {(0, 0): '0'}
        self.next_x = self.x
        self.next_y = self.y + 1
        self.forward, self.backwards, self.right, self.left = None, None, None, None
        self.maze_runner = mr

    def turn_left(self):
        directions_names = {'South': 'East',
                            'East': 'North',
                            'North': 'West',
                            'West': 'South'}
        directions_coords = {'South': (1, 0),
                            'East': (0, -1),
                            'North': (-1, 0),
                            'West': (0, 1)}
        self.next_x = self.x + directions_coords.get(self.direction)[0]
        self.next_y = self.y + directions_coords.get(self.direction)[1]
        self.direction = directions_names.get(self.direction)

        self.left = self.backwards
        self.backwards = self.right
        self.right = self.forward
        self.forward = self.maze_map.get((self.next_x, self.next_y))


        #print 'Turning left'

        self.maze_runner.turn_right()

    def turn_right(self):
        directions = {'South': 'West',
                      'East': 'South',
                      'North': 'East',
                      'West': 'North'}
        directions_coords = {'South': (-1, 0),
                            'East': (0, 1),
                            'North': (1, 0),
                            'West': (0, -1)}
        self.next_x = self.x + directions_coords.get(self.direction)[0]
        self.next_y = self.y + directions_coords.get(self.direction)[1]
        self.direction = directions.get(self.direction)

        self.left = self.forward
        self.backwards = self.left
        self.right = self.backwards
        self.forward = self.maze_map.get((self.next_x, self.next_y))


        #print 'Turning right'

        self.maze_runner.turn_left()

    def scan(self):
        for turns in range(4):
            #print 'Position ({}, {}) value is {}'.format(self.next_x, self.next_y, self.maze_map.get((self.next_x, self.next_y)))
            self.forward = self.maze_map.get((self.next_x, self.next_y))
            if (self.maze_map.get((self.next_x, self.next_y)) is None) & (self.maze_runner.found() is False):
                self.maze_map[(self.next_x, self.next_y)] = 'X'
                self.forward = self.maze_map.get((self.next_x, self.next_y))
                #print 'Setting ({}, {}) to x'.format(self.next_x, self.next_y)
            #elif (self.maze_map.get((self.next_x, self.next_y)) is None) & (self.maze_runner.found() is True):
            elif self.maze_runner.found() is True:
                #self.maze_runner.go()
                self.maze_map[(self.x, self.y)] = '#'
                #print 'FOUND!'
                return True
            self.turn_left()

        return False

    def go(self):
        #self.scan()
        if self.maze_runner.go() == True:
            #print 'Moving in {} direction from {}, {} to {}, {}'.format(self.direction, self.x, self.y, self.next_x, self.next_y)
            self.x = self.next_x
            self.y = self.next_y
            directions_coords = {'South': (0, 1),
                            'East': (1, 0),
                            'North': (0, -1),
                            'West': (-1, 0)}
            self.next_x = self.x + directions_coords.get(self.direction)[0]
            self.next_y = self.y + directions_coords.get(self.direction)[1]
            self.maze_map[(self.x, self.y)] = '0'
            self.backwards = '0'
            return True
        else:
            #print "Can't move to ({}, {})".format(self.next_x, self.next_y)
            self.maze_map[(self.next_x, self.next_y)] = '1'
            return False

    def report(self):
        print '========== Balli-3000 report =========='
        print 'Current coordinates (x, y):\t\t{}, {}'.format(self.x, self.y)
        print 'Current direction:\t\t\t\t{}'.format(self.direction)
        print 'Next coordinates (x, y):\t\t{}, {}'.format(self.next_x, self.next_y)
        print 'Forward: {}\tLeft: {}\tBackwards: {}\tRight: {} \t\t'.format(self.forward, self.left, self.backwards, self.right)
        print '=========== End of  report ============'

    def get_map(self):
        map = []

        for i in range(30):
            line = []
            for j in range(30):
                line.append('.')
            map.append(line)

        for position in self.maze_map.keys():
            x = 15 + position[0]
            y = 15 + position[1]
            map[y][x] = self.maze_map[position]

        return map

def maze_controller(mr):
    x, y = 0, 0

    balli = robot(mr)

    counter = 0
    while (not balli.scan()) & (counter < 1000):
        counter += 1
        if balli.left == 'X':
            balli.turn_left()
            #balli.scan()
            balli.go()
        elif balli.forward == 'X':
            #balli.scan()
            balli.go()
        elif balli.right == 'X':
            balli.turn_right()
            #balli.scan()
            balli.go()
        elif (balli.left == '0') & (balli.forward == '0') & (balli.right == '0'):
            #balli.scan()
            balli.turn_right()
            balli.go()
        else:
            balli.turn_left()
            if not balli.go():
                balli.turn_right()
                if not balli.go():
                    balli.turn_right()
        '''
        #balli.report()
        if balli.scan():
            for line in  balli.get_map():
                print line
            #balli.report()
            break
        else:
            pass
            #for line in  balli.get_map():
            #    print line
        #print ''
        '''
'''
    for line in  balli.get_map():
                print line
'''
        #balli.report()







list = [maze_example1,
        maze_example2,
        maze_example3,
        maze_example4,
        maze_example5,
        maze_example6,
        maze_example7,
        maze_example8,
        maze_example9,
        maze_example10,
        maze_example11,
        maze_example12,
        maze_example13,
        maze_example14,
        maze_example15
]
for i in list:
    maze_runner = MazeRunner(i['m'], i['s'], i['f'])
    maze_controller(maze_runner)
    print maze_runner.found()   # True

#maze_runner = MazeRunner(maze_example13['m'], maze_example13['s'], maze_example13['f'])
#maze_controller(maze_runner)
#print maze_runner.found()   # True


'''
maze_runner = MazeRunner(maze_example1['m'], maze_example1['s'], maze_example1['f'])
maze_controller(maze_runner)
print maze_runner.found()   # True

maze_runner = MazeRunner(maze_example2['m'], maze_example2['s'], maze_example2['f'])
maze_controller(maze_runner)
print maze_runner.found()   # True

maze_runner = MazeRunner(maze_example3['m'], maze_example3['s'], maze_example3['f'])
maze_controller(maze_runner)
print maze_runner.found()   # True

maze_runner = MazeRunner(maze_example4['m'], maze_example4['s'], maze_example4['f'])
maze_controller(maze_runner)
print maze_runner.found()   # True

maze_runner = MazeRunner(maze_example5['m'], maze_example5['s'], maze_example5['f'])
maze_controller(maze_runner)
print maze_runner.found()   # True

maze_runner = MazeRunner(maze_example6['m'], maze_example6['s'], maze_example6['f'])
maze_controller(maze_runner)
print maze_runner.found()   # True

maze_runner = MazeRunner(maze_example7['m'], maze_example7['s'], maze_example7['f'])
maze_controller(maze_runner)
print maze_runner.found()   # True

maze_runner = MazeRunner(maze_example8['m'], maze_example8['s'], maze_example8['f'])
maze_controller(maze_runner)
print maze_runner.found()   # True

maze_runner = MazeRunner(maze_example9['m'], maze_example9['s'], maze_example9['f'])
maze_controller(maze_runner)
print maze_runner.found()   # True

maze_runner = MazeRunner(maze_example10['m'], maze_example10['s'], maze_example10['f'])
maze_controller(maze_runner)
print maze_runner.found()   # True

maze_runner = MazeRunner(maze_example11['m'], maze_example11['s'], maze_example11['f'])
maze_controller(maze_runner)
print maze_runner.found()   # True

maze_runner = MazeRunner(maze_example12['m'], maze_example12['s'], maze_example12['f'])
maze_controller(maze_runner)
print maze_runner.found()   # True

maze_runner = MazeRunner(maze_example13['m'], maze_example13['s'], maze_example13['f'])
maze_controller(maze_runner)
print maze_runner.found()   # True

maze_runner = MazeRunner(maze_example14['m'], maze_example14['s'], maze_example14['f'])
maze_controller(maze_runner)
print maze_runner.found()   # True
'''