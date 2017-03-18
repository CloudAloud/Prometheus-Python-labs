__author__ = 'minin'

class SuperStr(str):

    def __init__(self, inputLine):
        self.input = str(inputLine).lower()

    def is_repeatance(self,s):
        if (type(s) != str) | (s == ''):
            return False

        checkString = ''
        i = 0
        while i < 100:
            i += 1
            checkString += s
            if checkString == self.input:
                return True

        return False

    def is_palindrom(self):
        reverseLine = list(self.input[:])
        reverseLine.reverse()
        if reverseLine == list(self.input[:]):
            return True
        else:
            return False

s = SuperStr('123123123123')
print s.is_repeatance('123') # True
print s.is_repeatance('123123') # True
print s.is_repeatance('123123123123') # True
print s.is_repeatance('12312') # False
print s.is_repeatance(123) # False
print s.is_palindrom() # False
print s # 123123123123
print int(s) # 123123123123
print s + 'qwe' # 123123123123qwe
p = SuperStr('123_321')
print p.is_palindrom() # True