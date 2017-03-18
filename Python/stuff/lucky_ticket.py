__author__ = 'minin'

import sys

first = int(sys.argv[1])
last = int(sys.argv[2])
sum = 0
def convert(rawinput):
    input = str(rawinput)
    output = [0,0,0,0,0,0]
    for number in range(len(input)):
        output[number-len(input)] = input[number]
    return output


for number in range(first,last+1):
    array = convert(number)
    part1 = int(array[0]) + int(array[1]) + int(array[2])
    part2 = int(array[3]) + int(array[4]) + int(array[5])
    if part1 == part2:
        sum = sum + 1
print sum