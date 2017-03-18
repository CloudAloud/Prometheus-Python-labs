__author__ = 'minin'

import datetime
import unittest

class MyTests(unittest.TestCase):

    def setUp(self):
        pass

#extract_words section
    def test_create_calendar_page_1(self):
        self.assertEqual(create_calendar_page(01, 1988), '--------------------\
MO TU WE TH FR SA SU\
--------------------\
			01 02 03\
04 05 06 07 08 09 10\
11 12 13 14 15 16 17\
18 19 20 21 22 23 24\
25 26 27 28 29 30 31')

def create_calendar_page(month=datetime.datetime.today().month, year=datetime.datetime.today().year):

    heading = '--------------------\n' \
             'MO TU WE TH FR SA SU\n' \
             '--------------------\n'
    normalWeek = ['MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU']
    monthList = []

    for day in range(1,33):
        #print day
        try:
            #dayOfWeek = datetime.date(year, month, day).weekday()
            monthList.append(normalWeek[datetime.date(year, month, day).weekday()])
            lastDay = day
        except ValueError:
            pass

        #monthList.append(normalWeek[dayOfWeek])


    week = ''

    if monthList[0] == 'TU':
        week = ' ' * 2
    elif monthList[0] == 'WE':
        week = ' ' * 5
    elif monthList[0] == 'TH':
        week = ' ' * 8
    elif monthList[0] == 'FR':
        week = ' ' * 11
    elif monthList[0] == 'SA':
        week = ' ' * 14
    elif monthList[0] == 'SU':
        week = ' ' * 17

    while len(monthList) > 0:
        number = lastDay - len(monthList) + 1
        if monthList[0] == 'SU':
            if number < 10:
                week = week + ' 0' + str(number) + '\n'
            else:
                week = week + ' ' + str(number) + '\n'
        elif monthList[0] == 'MO':
            if number < 10:
                week = week + '0' + str(number)
            else:
                week = week + str(number)
        else:
            if number < 10:
                week = week + ' 0' + str(number)
            else:
                week = week + ' ' + str(number)
        monthList.pop(0)


    return heading + week


#print create_calendar_page(01, 1988)
#print create_calendar_page(1, 1988)
#print create_calendar_page(9, 1939)
#print create_calendar_page(12, 2019)
print create_calendar_page(1, 2020)

#unittest.main()
#print datetime.date(2015,1,32)