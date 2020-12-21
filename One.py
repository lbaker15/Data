def sqrt(number):
    if number == 1:
        return 1
    end = number // 2
    begin = 0
    while (begin <= end):
        average = (begin + end) // 2
        sqr = average * average
        print(begin, end, number, sqr)
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
