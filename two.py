
def rotated_array_search(items, numberSearch, begin):
    end = len(items) - 1
    mid = begin + end // 2

    if items[mid] == numberSearch:
        print("FOUND", mid + end)
        return mid + end - 1
    if mid == begin == end:
        return -1
    else:
        #items are in order left side
        if items[begin] <= items[mid]:
            #print(items[mid+1], end, numberSearch)
            #in the first half
            if items[begin] <= numberSearch <= items[mid]:
                print(items[:mid])
                return rotated_array_search(items[:mid], numberSearch, begin)
            #in the second half
            else:
                print(items[mid:], items[mid+1:])
                return rotated_array_search(items[mid+1:], numberSearch, begin)
        #items not in order left side
        else:
            #in the second half
            if items[mid+1] <= numberSearch <= items[end]:
                print("HERE", items[mid:], items[mid+1:])
                return rotated_array_search(items[mid+1:], numberSearch, begin)
            #in the first half
            else:
                return rotated_array_search(items[:mid], numberSearch, begin)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            print(index)
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    #priorEnd = int(len(input_list) - 1)
    rotated_array_search(input_list, number, 0)
    """
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("WORKED", rotated_array_search(input_list, number))
    else:
        print("NOT WORKED", rotated_array_search(input_list, number))
    """


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 4])
#test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
#test_function([[6, 7, 8, 1, 2, 3, 4], 8])
#test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
#test_function([[], 0])
#test_function([[0], 0])

