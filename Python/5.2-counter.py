__author__ = 'minin'

def clean_list(inputList):
    n = 0
    while n < len(inputList):
        value = inputList[n]
        N = n + 1
        while N < len(inputList):
            if (value == inputList[N]) & (type(value) == type(inputList[N])):
                del inputList[N]
            else:
                N += 1
        n += 1
    return inputList

def counter(a, b):
    a = clean_list(list(str(a)))
    b = str(b)
    functionCounter = 0
    for number in a:
        if b.count(number) > 0:
            functionCounter += 1
    return functionCounter

print counter(1233211, 12128)