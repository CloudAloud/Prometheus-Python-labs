__author__ = 'minin'


class Student:
    def __init__(self, name, conf={'exam_max': 30, 'lab_max': 7, 'lab_num': 10, 'k': 0.61, }):
        self.name = name
        self.exam = 0
        self.k = conf['k']
        self.lab_max = conf['lab_max']
        self.lab_num = conf['lab_num']
        self.exam_max = conf['exam_max']
        self.labs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


    def make_lab(self, m, n=-1):
        if n == -1:
            n = self.labs.index(0)


        if m > self.lab_max:
            m = self.lab_max

        self.labs[n] = m

        return self



    def make_exam(self, m):
        if m > self.exam_max:
            self.exam = self.exam_max
        else:
            self.exam = m

        return self

    def is_certified(self):
        self.summ = 0
        for i in range(self.lab_num):
            if self.labs[i] <= self.lab_max:
                self.summ += self.labs[i]

        self.summ += self.exam


        if (float(self.summ) / (float(self.lab_max) * float(self.lab_num) + float(self.exam_max))) >= self.k:
        #if (float(self.summ) / (float(self.lab_max) * float(self.lab_num))) >= self.k:

            return (self.summ, True)
        else:
            return (self.summ, False)


#minin = Student('Anton', {'exam_max': 40, 'lab_max': 7, 'lab_num': 10, 'k': 0.61, })

conf1 = {'exam_max': 20,'lab_max': 40,'lab_num': 2,'k': 0.75}       #OK
o1 = Student('Oleg', conf1)                                         #OK
o1.is_certified()                                                   #OK (0, 0)
o2 = Student('Oleg', conf1)                                         #OK
o2.make_lab(60).make_lab(35.2)                                  #None
o2.is_certified()                                         #(75.2, True)

o3 = Student('Oleg', conf1)                                         #OK
o3.make_lab(10).make_lab(10).make_exam(15)                      #None
o3.is_certified()                                               #(35, False)
o3.make_lab(20,1).make_lab(20,0)                                #None
o3.is_certified()                                               #(55, False)
o3.make_lab(50,2)                                                   #OK
o3.is_certified()                                               #(55, False)
o3.make_lab(40,1)                                                   #OK
o3.is_certified()                                               #(75, True)
conf2 = {'exam_max': 52,'lab_max': 8,'lab_num': 6,'k': 0.5}         #OK
o4 = Student('Oleg', conf2)                                         #OK
o4.make_exam(100)                                               #None
o4.is_certified()                                               #(52, True)
o5 = Student('Oleg', conf2)                                         #OK
o5.make_lab(40).make_lab(7,5).make_lab(1).make_lab(7).make_lab(7).make_lab(7).make_lab(7,1) #None

#print o5.labs
#print o5.exam

print o5.is_certified()                                               #(43, False)
o5.make_lab(7)                                                      #OK
o5.is_certified()                                               #(43, False)
o5.make_exam(7)                                                 #None
conf3 = {'exam_max': 10,'lab_max': 1,'lab_num': 90,'k': 0.5,}       #OK
o6 = Student('Oleg', conf3)                                         #OK
for i in range(51): o6.make_lab(1)                              #None
o6.labs
o6.is_certified()                                               #(51, True)



# print minin.name, minin.conf['exam_max']
