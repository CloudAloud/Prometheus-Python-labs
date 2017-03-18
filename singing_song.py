__author__ = 'minin'

import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])


preverse = "la-" * x
verse = preverse[0:(len(preverse)-1)]

prestring = (verse + " ") * y
string = prestring[0:(len(prestring)-1)]

if z == 1:
    sign = "!"
else:
    sign = "."

if x * y == 0:
    presign = ""
else:
    presign = " "

print "Everybody sing a song:" + presign + string + sign