def merge_sort(data_list):
    """
    Sort data in the list in ascending order
    Returns a new sorted list

    How???
    Divide: Find midpoint of the list and split into two sublists
    Conquer: Use resursion - Sort the list recursively until len(list) <= 1
    Combine: Merge back the sorted list created in above step

    Takes (split_list + merge_list) i.e. O(n log n) time
    """
    #! Stopping point of recursion
    if len(data_list) <= 1:
        return data_list

    left_half, right_half = split_list(data_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge_list(left, right)


def split_list(listt):
    """
    Divide given list at midpoint into two sublists
    Takes O(log n) time overall
    """
    midpoint = len(listt) // 2
    left_part = listt[:midpoint]
    right_part = listt[midpoint:]
    return left_part, right_part


def merge_list(left_list, right_list):
    """
    Sort and merge the given two halves of the list
    Takes O(n) time
    """
    sorted_list = []
    i = 0
    j = 0

    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            sorted_list.append(left_list[i])
            i += 1
        else:  # left_list[i] >= right_list[j]
            sorted_list.append(right_list[j])
            j += 1

    while i < len(left_list):
        sorted_list.append(left_list[i])
        i += 1

    while j < len(right_list):
        sorted_list.append(right_list[j])
        j += 1

    return sorted_list


def verify_sorted(sorted_list):
    n = len(sorted_list)
    if n <= 1:
        return True

    return sorted_list[0] <= sorted_list[1] and verify_sorted(sorted_list[1:])


if __name__ == "__main__":
    # data = [12, 34, 55, 65, 77, 8, 9, 123, 344, 9]
    data = [12, 34, 55, 65,]
    is_sorted = verify_sorted(data)
    print(f"Is List Sorted? --> {is_sorted}")

    sorted_data = merge_sort(data)
    is_sorted = verify_sorted(sorted_data)
    print(f"Is List Sorted? --> {is_sorted}")
    print(sorted_data)