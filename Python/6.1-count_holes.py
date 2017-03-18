__author__ = 'minin'


def count_holes(n):
    if (type(n) == int) | (type(n) == str) | (type(n) == long):
        counter = 0
        try:
            int(n)
        except:
            return 'ERROR'

        for number in str(int(n))[:]:
            if (number == '0') | (number == '4' ) | (number == '6' ) | (number == '9'):
                counter += 1
            elif number == '8':
                counter += 2
        return counter
    else:
        return 'ERROR'
print count_holes('123')
print count_holes(906)
print count_holes('001')
print count_holes(-8)
print count_holes(-8.0)

print count_holes(1)
print count_holes(0)
print count_holes(1234)
print count_holes('000000000010')
print count_holes('00000000001')
print count_holes(888888888888888888888)
print count_holes(-888888888888888888888)
print count_holes('888888888888888888888')
print count_holes(888888888888888888888.0)

print count_holes(69L)
print count_holes([1])
print count_holes(None)
print count_holes('qq')
print count_holes('')
print count_holes('888888888888888888888.0')
'''
0
3
0
2
ERROR
0
1
1
1
0
42
42
42
ERROR
ERROR
ERROR
2
ERROR
ERROR
ERROR
'''
