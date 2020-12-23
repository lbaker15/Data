def sqrt(number):
    if number < 0 :
        test = str(number).split('-')
        number = int(test[1])
    if number == 1:
        return 1
    end = number // 2
    begin = 0
    while (begin <= end):
        average = (begin + end) // 2
        sqr = average * average
        if (sqr == number):
            return average
        elif (number > sqr):
            result = average
            begin = average + 1
        elif (number < sqr):
            end = average - 1
    return result

#print ("Pass" if  (3 == sqrt(9)) else "Fail")
#print ("Pass" if  (0 == sqrt(0)) else "Fail")
#print ("Pass" if  (4 == sqrt(16)) else "Fail")
#print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (2 == sqrt(-4)) else "Fail")
print ("Pass" if  (64 == sqrt(4096)) else "Fail")

