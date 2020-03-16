import sys


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) <= 0:
        print("Please input a non-empty array!")
        return None
    min = sys.maxsize
    max = -(sys.maxsize - 1)
    for i in ints:
        if i >= max:
            max = i
        if i <= min:
            min = i
    return (min, max)


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

# Test code below
# Test Case 1 - Normal case
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Test Case 2 - Edge case - zero element
print(get_min_max([]))  # None and print a warning "Please input a non-empty array!"

# Test Case 2 - Edge case - single element
print(get_min_max([0]))  # (0, 0)
