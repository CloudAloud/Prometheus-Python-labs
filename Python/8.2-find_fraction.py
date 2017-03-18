__author__ = 'minin'

def find_bcd(a, b):
    while (a != 0) & (b != 0):
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

def find_fraction(summ):
    if summ > 1:
        a = int(summ) / 2
        b = int(summ) - a
    else:
        return False

    while find_bcd(a, b) != 1:
        a -= 1
        b = int(summ) - a

    if a != b:
        return a, b
    else:
        return False

print find_fraction(2) # False
print find_fraction(3) # (1, 2)
print find_fraction(10) # (3, 7)
print find_fraction(62) # (29, 33)
print find_fraction(150000001) # (75000000, 75000001)
