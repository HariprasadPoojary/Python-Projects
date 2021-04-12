from linked_list import LinkedList


def merge_sort(linked_list):
    """
    Sorts Linked List in ascending order
    - Recursively divide LinkedList into sublist containing a single node
    - Repeatedly merge the sublists to produce sorted sublists until one remains
    Returns a sorted LinkedList
    """
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split_list(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge_list(left, right)


def split_list(linked_list):
    """
    Divide unsorted LinkedList at midpoint into sublists
    """

    if linked_list is None or linked_list.head is None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        midpoint = linked_list.size() // 2
        mid_node = linked_list.node_at_index(midpoint - 1)
        # split the LinkedList on Midpoint
        # ? right
        right_half = LinkedList()  # create new instance
        right_half.head = mid_node.next_node  # start after midpoint
        # ? left
        left_half = linked_list
        mid_node.next_node = None  # stop on midpoint

        return left_half, right_half
