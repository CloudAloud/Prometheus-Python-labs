__author__ = 'minin'

import sys

input = sys.argv[1].replace(" ", "").lower()

string = []
antistring = []

for n in range(len(input)):
    string.append(input[n])
    antistring.append(input[n])

antistring.reverse()

if string == antistring:
    print "YES"
else:
    print "NO"