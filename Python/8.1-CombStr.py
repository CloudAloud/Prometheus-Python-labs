__author__ = 'minin'

class CombStr(str):

    def __init__(self, inputLine):
        self.input = str(inputLine)

    def count_substrings(self, lenght):
        if (lenght == 0) | (lenght > len(self.input)):
            return 0

        array = []
        for i in range(len(self.input) - lenght + 1):
            if array.count(self.input[i:i+lenght]) == 0:
                array.append(self.input[i:i+lenght])

        #return array
        return len(array)





s0 = CombStr('qqqqqqweqqq%')
print s0.count_substrings(0) # 0
print s0.count_substrings(1) # 4
print s0.count_substrings(2) # 5
print s0.count_substrings(5) # 7
print s0.count_substrings(15) # 0