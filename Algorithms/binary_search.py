def binary_search(listt, target, low=None, high=None):
    """
    returns index value of the target from list using binary search
    """
    # setting high and low values if they are None
    if low is None:
        low = 0
    if high is None:
        high = len(listt) - 1

    if high < low:  # target is not in the list
        return -1

    # sample list values [1,2,3,4,5,6,7,8,9], target = 6

    # find the midpoint (suited for every recursive loop)
    midpoint = (low + high) // 2

    if listt[midpoint] == target:  # midpoint is the target
        return midpoint
    elif target < listt[midpoint]:
        # ignore the right values from the midpoint(using high and low) and recurse the function again
        return binary_search(listt, target, low, midpoint - 1)
    elif target > listt[midpoint]:
        # ignore the left values from the midpoint(using high and low) and recurse the function again
        return binary_search(listt, target, midpoint + 1, high)


if __name__ == "__main__":
    l = [1, 2, 3, 4, 12, 13, 14, 15, 23, 24, 35, 46, 67, 68, 69, 70, 71, 89, 90]
    target = 23
    print(binary_search(l, target))
