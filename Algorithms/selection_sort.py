def selection_sort(data_list):
    # loop till length of list
    sorted_list = []
    index = 0  # Track location/index to pop element
    for i in range(len(data_list)):
        min_value = data_list[0]  # default 1st element as smallest
        for j in range(len(data_list)):
            # compare data to min value
            if data_list[j] < min_value:
                min_value = data_list[j]
                index = j  # this element must be added to sorted and removed from original list

        if min_value == data_list[0]:  # if default min value is the smallest no.
            index = 0
        # add min_value to sorted_list and remove same from data_list
        sorted_list.append(data_list.pop(index))

    return sorted_list


if __name__ == "__main__":
    data = [12, 34, 55, 65, 77, 8, 9, 123, 344, 9]
    print(selection_sort(data))
