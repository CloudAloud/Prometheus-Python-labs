__author__ = 'minin'

import sys

list = sys.argv[1:]
result = ""
list.reverse()

for argument in list:
    result = result + argument + " "

print result[:-1]