__author__ = 'minin'

import sys

input = sys.argv[1]
sum = 0

for argument in range(len(input)):
    if sum >= 0:
            if input[argument] == ")":
                sum = sum - 1
            elif input[argument] == "(":
                sum = sum + 1
    else:
        verdict = "NO"
if sum == 0:
    verdict = "YES"
else:
    verdict = "NO"

print verdict