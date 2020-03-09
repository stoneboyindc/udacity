def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        print("Please pass in a none negative number!")
        return number
    if number == 1:
        return number
    divider = 2
    midpoint = number // divider
    while True:
        if midpoint * midpoint <= number:
            break
        else:
            divider += 1
            midpoint = number // divider
    return midpoint


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")

