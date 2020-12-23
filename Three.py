def rearrange_digits(input_list):
    if len(input_list) < 2:
        return None
    quicksort(input_list)
    result = [''] * 2
    for i in range(len(input_list) - 1, -1, -1):
        if i%2 == 0:
            if i == len(input_list) - 1:
                result[0] = result[0] + str(input_list[i])
            else:
                result[1] = result[1] + str(input_list[i])
        else:
            result[0] = result[0] + str(input_list[i])
    mylist = list(map(int, result))
    return mylist

def quicksort(items):
    sort_all(items, 0, len(items) - 1)

def sort_all(items, begin, end):
    if end <= begin:
        return
    pivot_index = sort_a_little_bit(items, begin, end)
    sort_all(items, begin, pivot_index - 1)
    sort_all(items, pivot_index + 1, end)

def sort_a_little_bit(items, begin_index, end_index):
    left_index = begin_index
    pivot_index = end_index
    pivot_value = items[pivot_index]
    while (pivot_index != left_index):
        item = items[left_index]
        #item begin item, pivot_value end item
        if item <= pivot_value:
            left_index += 1
            continue
        #Begin becomes item before last
        items[left_index] = items[pivot_index - 1]
        #Item before last becomes last item value
        items[pivot_index - 1] = pivot_value
        #Last item becomes beginning item
        items[pivot_index] = item
        pivot_index -= 1
    return pivot_index

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if output == None:
        print("Please enter a longer list")
        return
    print(output, solution)
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
test_function([[1], [1]])