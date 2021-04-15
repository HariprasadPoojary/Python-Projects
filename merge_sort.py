def merge_sort(data_list):

    # stopping point, base case
    if len(data_list) <= 1:
        return data_list

    # Get mid point to divide the list
    mid_index = len(data_list) // 2

    left_half = data_list[:mid_index]
    right_half = data_list[mid_index:]

    # further divide the list into left and right chunks until base case
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    # sorting setup
    sorted_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    # there is a chance that left or right still has values left in them
    # add those remaining values to the sorted list
    sorted_list += left[left_index:]
    sorted_list += right[right_index:]

    return sorted_list


if __name__ == "__main__":
    data = [34, 12, 80, 65]
    print(merge_sort(data))