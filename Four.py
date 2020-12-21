def sortNum(input_list):
    end = len(input_list) - 1
    front = 0
    next = 0
    while front < end:
        curr = input_list[front]
        if curr == 0:
            #Reassign next along from first zero to 0 and current value to the value that existed at next before reassigning
            value = input_list[next]
            input_list[next] = 0
            input_list[front] = value
            next +=1
            front += 1
        elif curr == 2:
            #Reassigning the value before the end - swap with front which is always 2
            value = input_list[end]
            input_list[end] = 2
            input_list[front] = value
            end -= 1
        else:
            front += 1
    print(input_list)
    return input_list

def test_function(test_case):
    sorted_array = sortNum(test_case)
    """
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")
    """

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])