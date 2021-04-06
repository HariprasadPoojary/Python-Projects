class Node:
    """
    An object for storing single node of linked list
    Has 2 attributes - data and the link to the next node in the list
    """

    data = None
    next_node = None

    def __init__(self, data) -> None:
        self.data = data

    def __repr__(self) -> str:
        return f"<Node data: {self.data}>"


class LinkedList:
    """
    Singly Linked List
    """

    def __init__(self) -> None:
        self.head = None

    def is_empty(self) -> bool:
        return self.head == None

    def size(self) -> int:
        """
        Returns the number of nodes in the List
        Takes O(n) time
        """
        current = self.head
        cnt = 0
        # loop till next_node doesn't exists
        while current:
            cnt += 1  # increment the count
            current = current.next_node  # assign next node to cuurent

        return cnt

    def add(self, data) -> None:
        """
        Adds new node to the head of the list
        Takes O(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def l_print(self) -> None:
        current = self.head
        # loop till next_node doesn't exists
        while current:
            print(current)  # print the node
            current = current.next_node  # assign next node to cuurent


l = LinkedList()
l.add(20)
l.add(30)
l.add(40)
l.add(50)

l.l_print()