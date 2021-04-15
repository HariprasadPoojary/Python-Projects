def quick_sort(data_list):
    if len(data_list) <= 1:
        return data_list

    # initialize values
    pivot = data_list[0]
    less_than_pivot = []
    more_than_pivot = []

    for data in data_list[1:]:
        if data < pivot:
            less_than_pivot.append(data)
        else:
            more_than_pivot.append(data)

    return quick_sort(less_than_pivot) + [pivot] + quick_sort(more_than_pivot)


if __name__ == "__main__":
    data = [34, 12, 80, 65]
    print(quick_sort(data))
