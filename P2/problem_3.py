def partition(arr, low, high):
    i = low - 1  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than the pivot
        if arr[j] < pivot:

            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    quickSort(input_list, 0, len(input_list) - 1)
    # print("after quickSort: ", input_list)
    a = 0
    b = 0
    # for i in range(0, len(input_list)):
    for i in range(len(input_list) - 1, -1, -1):
        if i % 2 == 0:
            a = a * 10 + input_list[i]
        else:
            b = b * 10 + input_list[i]
    return a, b


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    # print("output:", output)
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Test code below
# Test Case 1 - Normal case
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

# Test Case 2 - Edge case: Every element are the same
print(rearrange_digits([1, 1, 1, 1, 1, 1, 1]))  # (1111, 111)

# Test Case 3 - Edge case: an array of single element
print(rearrange_digits([1]))  # (1, 0)

