__author__ = 'minin'

import unittest
import final_maze_controller

class MyTests(unittest.TestCase):

    def setUp(self):
        pass

# Test turn functions
    def test_left_turns(self):
        balli = final_maze_controller.robot()

        # Turn left 4 times
        self.assertEqual(balli.x, 0)
        self.assertEqual(balli.y, 0)
        self.assertEqual(balli.next_x, 0)
        self.assertEqual(balli.next_y, 1)
        self.assertEqual(balli.direction, 'South')

        balli.turn_left()
        self.assertEqual(balli.x, 0)
        self.assertEqual(balli.y, 0)
        self.assertEqual(balli.next_x, 1)
        self.assertEqual(balli.next_y, 0)
        self.assertEqual(balli.direction, 'East')

        balli.turn_left()
        self.assertEqual(balli.x, 0)
        self.assertEqual(balli.y, 0)
        self.assertEqual(balli.next_x, 0)
        self.assertEqual(balli.next_y, -1)
        self.assertEqual(balli.direction, 'North')

        balli.turn_left()
        self.assertEqual(balli.x, 0)
        self.assertEqual(balli.y, 0)
        self.assertEqual(balli.next_x, -1)
        self.assertEqual(balli.next_y, 0)
        self.assertEqual(balli.direction, 'West')

        balli.turn_left()
        self.assertEqual(balli.x, 0)
        self.assertEqual(balli.y, 0)
        self.assertEqual(balli.next_x, 0)
        self.assertEqual(balli.next_y, 1)
        self.assertEqual(balli.direction, 'South')

        # Turn right 4 times
        self.assertEqual(balli.x, 0)
        self.assertEqual(balli.y, 0)
        self.assertEqual(balli.next_x, 0)
        self.assertEqual(balli.next_y, 1)
        self.assertEqual(balli.direction, 'South')

        balli.turn_right()
        self.assertEqual(balli.x, 0)
        self.assertEqual(balli.y, 0)
        self.assertEqual(balli.next_x, -1)
        self.assertEqual(balli.next_y, 0)
        self.assertEqual(balli.direction, 'West')

        balli.turn_right()
        self.assertEqual(balli.x, 0)
        self.assertEqual(balli.y, 0)
        self.assertEqual(balli.next_x, 0)
        self.assertEqual(balli.next_y, -1)
        self.assertEqual(balli.direction, 'North')

        balli.turn_right()
        self.assertEqual(balli.x, 0)
        self.assertEqual(balli.y, 0)
        self.assertEqual(balli.next_x, 1)
        self.assertEqual(balli.next_y, 0)
        self.assertEqual(balli.direction, 'East')

        balli.turn_right()
        self.assertEqual(balli.x, 0)
        self.assertEqual(balli.y, 0)
        self.assertEqual(balli.next_x, 0)
        self.assertEqual(balli.next_y, 1)
        self.assertEqual(balli.direction, 'South')

if __name__ == '__main__':
    unittest.main()