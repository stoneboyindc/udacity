# Returns index of x in arr if present, else -1
def binarySearch(arr, l, r, x):
    # Check base case
    if r >= l:
        mid = l + (r - l) / 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        # Else the element can only be present in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        # Element is not present in the array
        return -1


def findPivot(arr):
    return doFindPivot(arr, 0, len(arr) - 1)


def doFindPivot(arr, l, r):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] > arr[mid + 1]:
            return mid
        elif arr[mid] > arr[0]:
            return doFindPivot(arr, mid, r)
        else:
            return doFindPivot(arr, l, mid)
    else:
        return -1


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    result = -1
    pivotIdx = findPivot(input_list)
    if number == input_list[0]:
        return 0
    elif number > input_list[0]:
        result = binarySearch(input_list, 0, pivotIdx, number)
    else:
        result = binarySearch(input_list, pivotIdx + 1, len(input_list) - 1, number)
    return result


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# print(findPivot([6, 7, 8, 9, 10, 1, 2, 3, 4]))
# print(findPivot([6, 7, 8, 1, 2, 3, 4]))
# arr = [6, 7, 8, 9, 10, 1, 2, 3, 4]
# print(rotated_array_search(arr, 6))
# print(rotated_array_search(arr, 1))
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
