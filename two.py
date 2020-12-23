
def rotated_array_search(items, numberSearch, begin, num=0):
    end = len(items) - 1
    mid = (begin + end) // 2
    if items[mid] == numberSearch:
        return mid + num
    if mid == begin == end:
        return -1
    else:
        #items are in order left side
        if items[begin] <= items[mid]:
            #in the first half
            if items[begin] <= numberSearch <= items[mid]:
                return rotated_array_search(items[:mid], numberSearch, begin, num)
            #in the second half
            else:
                return rotated_array_search(items[mid+1:], numberSearch, begin, mid+num+1)
        #items not in order left side
        else:
            #in the second half
            if items[mid+1] <= numberSearch <= items[end]:
                return rotated_array_search(items[mid+1:], numberSearch, begin, mid+num+1)
            #in the first half
            else:
                return rotated_array_search(items[:mid], numberSearch, begin, num)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            print(index)
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number, 0):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

