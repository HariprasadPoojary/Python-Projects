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


def merge_list(left, right):
    """
    Merges a two linked lists, sorting by data of the nodes
    Returns a new, merged list
    """
    # Creating a new LinkedList to store
    # left and right merged list
    merged = LinkedList()

    # Add a fake head which will be replaced with
    # node at zero index
    merged.add(0)

    # Set current to the fake head
    current = merged.head

    # Get head node of left and right list
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach tail node
    # of either lists
    while left_head or right_head:
        # If left_head is None then we're past the tail
        # Add node from right_head to merge list
        if left_head is None:
            current.next_node = right_head
            # Call next_node on right to exit loop i.e. right_head is None
            right_head = right_head.next_node

        # If right_head is None then we're past the tail
        # Add node from left_head to merge list
        elif right_head is None:
            current.next_node = left_head
            # Call next_node on left to exit loop i.e. left_head is None
            left_head = left_head.next_node

        else:  # not a tail node of either, perform comparison operation
            left_data = left_head.data
            right_data = right_head.data
            # if  left_data < right_data, set current.next_node to left node
            if left_data < right_data:
                current.next_node = left_head
                # Move left head to next node
                left_head = left_head.next_node
            else:  # right_data < left_data, set current.next_node to right node
                current.next_node = right_head
                # Move right head to next node
                right_head = right_head.next_node

        # Move current to next node
        current = current.next_node

    # Discard fake head and set it to fake head's next_node
    merged.head = merged.head.next_node

    return merged


if __name__ == "__main__":
    data = [12, 34, 55, 65, 77, 8, 9, 123, 344, 9]
    l = LinkedList()
    for i in data:
        l.add(i)

    print(merge_sort(l))
