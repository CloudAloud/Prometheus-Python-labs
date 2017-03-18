__author__ = 'minin'

import unittest


class MyTests(unittest.TestCase):

    def setUp(self):
        pass

#normalize
    def test_normalize_1(self):
        self.assertEqual(normalize(1), '1')

    def test_normalize_2(self):
        self.assertEqual(normalize('z'), 'Z')

    def test_normalize_3(self):
        self.assertEqual(normalize('A'), 'A')

    def test_normalize_4(self):
        self.assertEqual(normalize('4'), '4')

    def test_normalize_10(self):
        self.assertEqual(normalize('VIX1F'), 'VIX1F')

    def test_normalize_11(self):
        self.assertEqual(normalize('-VIX1F'), '-VIX1F')


#convert_n_to_m
    def test_convert_n_to_m_1(self):
        self.assertEqual(convert_n_to_m('!', 4, 3), False)

    def test_convert_n_to_m_2(self):
        self.assertEqual(convert_n_to_m(['~'], 4, 3), False)

    def test_convert_n_to_m_3(self):
        self.assertEqual(convert_n_to_m(-123.0, 4, 3), False)

    def test_convert_n_to_m_4(self):
        self.assertEqual(convert_n_to_m('-1', 4, 3), False)

    def test_convert_n_to_m_5(self):
        self.assertEqual(convert_n_to_m('VIX1F', 4, 3), False)

    def test_convert_n_to_m_11(self):
        self.assertEqual(convert_n_to_m([123], 4, 3), False)

    def test_convert_n_to_m_12(self):
        self.assertEqual(convert_n_to_m("0123", 5, 6), '102')

    def test_convert_n_to_m_13(self):
        self.assertEqual(convert_n_to_m("123", 3, 5), False)

    def test_convert_n_to_m_14(self):
        self.assertEqual(convert_n_to_m(123, 4, 1), '000000000000000000000000000')

    def test_convert_n_to_m_15(self):
        self.assertEqual(convert_n_to_m(-123.0, 11, 16), False)

    def test_convert_n_to_m_16(self):
        self.assertEqual(convert_n_to_m("A1Z", 36, 16), '32E7')

    def test_convert_n_to_m_21(self):
        self.assertEqual(convert_n_to_m([1], 2, 2), False)

    def test_convert_n_to_m_22(self):
        self.assertEqual(convert_n_to_m(True, 1, 2), False)

    def test_convert_n_to_m_23(self):
        self.assertEqual(convert_n_to_m({1: 0}, 2, 2), False)

    def test_convert_n_to_m_24(self):
        self.assertEqual(convert_n_to_m(-777, 10, 2), False)

    def test_convert_n_to_m_25(self):
        self.assertEqual(convert_n_to_m(123123123123123123123.0, 11, 16), False)

    def test_convert_n_to_m_26(self):
        self.assertEqual(convert_n_to_m(100, 2, 1), '0000')

    def test_convert_n_to_m_27(self):
        self.assertEqual(convert_n_to_m(0, 10, 2), '0')

    def test_convert_n_to_m_28(self):
        self.assertEqual(convert_n_to_m(000, 10, 2), '0')

    def test_convert_n_to_m_29(self):
        self.assertEqual(convert_n_to_m('ZZZZ', 36, 13), '46A672')

    def test_convert_n_to_m_30(self):
        self.assertEqual(convert_n_to_m('000ZZZZ', 36, 13), '46A672')

    def test_convert_n_to_m_31(self):
        self.assertEqual(convert_n_to_m('ZZZZ', 35, 13), False)

    def test_convert_n_to_m_32(self):
        self.assertEqual(convert_n_to_m('qweasd', 33, 36), 'HGPEYJ')

    def test_convert_n_to_m_33(self):
        self.assertEqual(convert_n_to_m('123123123123123123123', 11, 16), '2C09BC518E8048D23A')

    def test_convert_n_to_m_34(self):
        self.assertEqual(convert_n_to_m(123123123123123123123, 11, 16), '2C09BC518E8048D23A')

    def test_convert_n_to_m_35(self):
        self.assertEqual(convert_n_to_m(123123123123123123123, 10, 10), '123123123123123123123')

    def test_convert_n_to_m_36(self):
        self.assertEqual(convert_n_to_m('bnh34521', 31, 14), '119337DC2BC')

    def test_convert_n_to_m_37(self):
        self.assertEqual(convert_n_to_m('bnh34521', 11, 14), False)

    def test_convert_n_to_m_38(self):
        self.assertEqual(convert_n_to_m('000', 10, 2), '0')

    def test_convert_n_to_m_39(self):
        self.assertEqual(convert_n_to_m(777, 10, 2), '1100001001')

    def test_convert_n_to_m_40(self):
        self.assertEqual(convert_n_to_m(777L, 10, 2), '1100001001')



alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def normalize(value):
    if type(value) == int:
        return str(value).upper()
    elif type(value) == long:
        return int(value)
    elif str(value).count('0') == len(value):
        return '0'
    else:
        return value.upper()

def check(value):
    if (type(value) == float) | (type(value) == list) | (type(value) == tuple) | (type(value) == bool) | (type(value) == dict):
        return False
    else:
        value = normalize(value)

    if value == '0':
        return '0'

    counter = 0

    for number in str(value):
        if alphabet.count(number) != 1:
            return False
        elif alphabet.count(number) == 1:
            counter += 1
        else:
            print 'Check Error!'

    return counter

def convert_n_to_m(x, n, m):
    #Stop if check isn't okay
    if not check(x):
        return False

    x = str(x).upper()


    if str(x).count('0') == len(x):
        return '0'

    if n == m:
        return x

    #Fill middleNumber
    middleNumber = []
    for position in range(len(x)):
        middleNumber.append(alphabet.index(x[position]))

    #Check if number is correct
    checkNumber = middleNumber[:]
    checkNumber.sort()

    if checkNumber.pop() >= n:
        return False

    #check if n > m or not

    #Convert the number into decimal
    decimalResult = 0
    for position in range(len(middleNumber[:])):
        power = len(middleNumber[:]) - position - 1
        if power == 0:
            decimalResult += middleNumber[position]
        else:
            decimalResult += middleNumber[position] * n ** power

    #Convert decimal into destination
    if m == 10:
        return decimalResult
    elif m == 1:
        result = ''
        while decimalResult > 0:
            result += '0'
            decimalResult -= 1
        return result
    else:
        result = []

        while decimalResult > 0:
            current = decimalResult % m
            decimalResult = decimalResult / m
            result.append(alphabet[current])
            #print current, decimalResult, result


    #Finalisation
    result.reverse()
    finalresult = ''
    for position in range(len(result)):
        finalresult += str(result[position])
    return finalresult

unittest.main()