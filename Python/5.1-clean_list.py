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

print clean_list([1, 1.0, '1', -1, 1])
