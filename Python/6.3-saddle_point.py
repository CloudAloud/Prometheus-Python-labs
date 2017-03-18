__author__ = 'minin'

import unittest


class MyTests(unittest.TestCase):

    def setUp(self):
        pass

#find_min section
    def test_find_min_0_1_2(self):
        self.assertEqual(find_min([0,1,2]), 0)

    def test_find_min_1_1_2(self):
        self.assertEqual(find_min([1,1,2]), False)

    def test_find_min_1_1_1(self):
        self.assertEqual(find_min([1,1,1]), False)

    def test_find_min_3_2_1(self):
        self.assertEqual(find_min([3,2,1]), 2)

    def test_find_min_3_21_1(self):
        self.assertEqual(find_min([1,21,1]), False)

    def test_find_min_3_21_1_0(self):
        self.assertEqual(find_min([1,21,1,0]), 3)

#find_max section

    def test_find_max_0_1_2(self):
        self.assertEqual(find_max([0,1,2]), 2)

    def test_find_max_1_1_2(self):
        self.assertEqual(find_max([1,1,2]), 2)

    def test_find_max_1_1_1(self):
        self.assertEqual(find_max([1,1,1]), False)

    def test_find_max_3_2_1(self):
        self.assertEqual(find_max([3,2,1]), 0)

    def test_find_max_3_21_1(self):
        self.assertEqual(find_max([1,21,1]), 1)

    def test_find_max_3_21_1_87(self):
        self.assertEqual(find_max([1,21,1,87]), 3)

    def test_find_max_2_2_1(self):
        self.assertEqual(find_max([2,2,1]), False)

#saddle_point section

    def test_saddle_point_123_021(self):
        self.assertEqual(saddle_point([[1,2,3],[0,2,1]]), (0,0))

    def test_saddle_point_123_321(self):
        self.assertEqual(saddle_point([[1,2,3],[3,2,1]]), False)

    def test_saddle_point_83012348123_32123947923_76013523411(self):
        self.assertEqual(saddle_point([[8,3,0,1,2,3,4,8,1,2,3],[3,2,1,2,3,9,4,7,9,2,3],[7,6,0,1,3,5,2,3,4,1,1]]), (1,2))

    def test_saddle_point_21(self):
        self.assertEqual(saddle_point([[21]]), (0,0))

    def test_saddle_point_000_212_101(self):
        self.assertEqual(saddle_point([[0,0,0],[2,1,2],[1,0,1]]), (1,1))

    def test_saddle_point_555_556_545(self):
        self.assertEqual(saddle_point([[5,5,5],[5,5,6],[5,4,5]]), False)

    def test_saddle_point_433_321_656(self):
        self.assertEqual(saddle_point([[4,3,3],[3,2,1],[6,5,6]]), (2,1))

    def test_saddle_point_123011_432112_432011_000001(self):
        self.assertEqual(saddle_point([[1,2,3,0,1,1],[4,3,2,1,1,2],[4,3,2,0,1,1],[0,0,0,0,0,1]]), False)

def find_min(line):
    minValue = 1000000
    minValuePosition = 10000
    lineString = ""

    for value in line:
        lineString += str(value)
    for position in range(len(line)):
        currentValue = line[position]
        if (minValue > currentValue):
            minValue = currentValue
            minValuePosition = position

    if (minValue == 1000000) | (lineString.count(str(minValue)) != 1):
        return False
    else:
        return minValuePosition

def find_max(line):
    maxValue = -1
    maxValuePosition = 0
    lineString = ""
    for value in line:
        lineString += str(value)

    for position in range(len(line)):
        currentValue = line[position]
        if (maxValue < currentValue):
            maxValue = currentValue
            maxValuePosition = position

    if (maxValue == -1) | (lineString.count(str(maxValue)) != 1):
        return False
    else:
        return maxValuePosition


def saddle_point(matrix):
    for line in matrix:
        linePosition = matrix.index(line)
        row = []
        position = find_min(line)

        for line in matrix:
            row.append(line[position])

        if (linePosition == find_max(row)) & (str(position) != 'False'):
            return linePosition, position

    return False

unittest.main()
#print find_max([2,2,1])