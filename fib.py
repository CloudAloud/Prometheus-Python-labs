__author__ = 'minin'

import sys

n = int(sys.argv[1])
a = 0
b = 1

for i in range(n):
    result = a + b
    a = b
    b = result
print a