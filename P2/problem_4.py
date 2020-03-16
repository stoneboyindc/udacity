def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    pVal = 1
    p0 = 0
    p1 = 0
    p2 = len(input_list) - 1
    # Scanning forward
    while p1 <= p2:
        if input_list[p1] == 0:
            input_list[p0], input_list[p1] = input_list[p1], input_list[p0]
            p0 += 1
            p1 += 1
        elif input_list[p1] == 1:
            p1 += 1
        else:
            input_list[p1], input_list[p2] = input_list[p2], input_list[p1]
            p2 = p2 - 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# Test code below
# Test Case 1 - Normal case
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function(
    [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
)
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Test Case 2 - Edge case - missing an element
print(sort_012([0, 0, 2, 2, 0, 2]))  # [0, 0, 0, 2, 2, 2]

# Test Case 3 - Edge case - missing two elements
print(sort_012([0, 0, 0]))  # [0, 0, 0]
