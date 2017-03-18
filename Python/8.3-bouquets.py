__author__ = 'minin'

def bouquets(narcissus_price, tulip_price, rose_price, summ):

    counter = 0

    for narcissus_count in range(0, int(summ / narcissus_price) + 1):
        left1 = summ - narcissus_count * narcissus_price
        #print 'Narcissus count: ' + str(narcissus_count)
        for tulip_count in range(0, int(left1 / tulip_price) + 1):
            left2 = left1 - tulip_count * tulip_price
            #print 'Tulip count: ' + str(tulip_count)
            for rose_count in range(0, int(left2 / rose_price) + 1):
                left3 = left2 - rose_count * rose_price
                #print 'Rose count: ' + str(rose_count)
                total_count = narcissus_count + tulip_count + rose_count
                if (total_count % 2 == 1) & (total_count != 0):
                    counter += 1
    return counter


print bouquets(1,1,1,5) # 34
print bouquets(2,3,4,10) # 12
print bouquets(2,3,4,100) # 4019
print bouquets(200,300,400,10000) # 4019
print bouquets(200,300,400,100000) # 3524556

print bouquets(1,1,1,10) # 125
print bouquets(1,2,1,10) # 79
print bouquets(2,1,1,10) # 79
print bouquets(3,4,5,2) # 0
print bouquets(3,4,5,3) # 1
print bouquets(3,4,5,5) # 3
print bouquets(15.5,4.1,5.99,21.75) # 8
print bouquets(21.25,13.6,10.5,100) # 51
print bouquets(10,199,99,20000) # 3462847
print bouquets(22,44,150,20000) # 4666877
