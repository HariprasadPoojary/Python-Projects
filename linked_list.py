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

    def search(self, key):
        """
        Returns Node object if 'key' is found in LinkedList object else None
        Takes O(n) time
        """
        current_node = self.head
        while current_node:
            if current_node.data == key:
                return current_node
            else:
                current_node = current_node.next_node
        return None

    def insert(self, data, index=None) -> bool:
        """
        Inserts the data in the given index or at the head id index is None
        Takes O(n) time to search for the index
        Takes O(1) time to insert the data
        Overall takes O(n) time
        """
        if index is None or index == 0:
            self.add(data)
            return True

        cnt = 1
        # as index 0 is self.head, we start from next node
        current_node = self.head.next_node
        prev_node = self.head  # to keep track of previous node
        while current_node:
            if index == cnt:
                new_node = Node(data)  # new node
                # place new node before current node i.e. on the index
                new_node.next_node = current_node
                # tag new node as next_node of current node - 1 node
                prev_node.next_node = new_node
                return True
            else:  # no match of index
                prev_node = current_node
                current_node = current_node.next_node
                cnt += 1

    def remove(self, data=None) -> bool:
        if data is None or data == self.head.data:
            new_head = self.head.next_node
            del self.head
            self.head = new_head

        # as index 0 is self.head, we start from next node
        current_node = self.head.next_node
        prev_node = self.head  # to keep track of previous node
        current_next_node = current_node.next_node
        while current_node:
            if data == current_node.data:
                # assign previous node's next node to - next node of cuurent node 😅
                prev_node.next_node = current_next_node
                del current_node  # delete current node
                return True
            else:
                prev_node = current_node
                current_node = current_node.next_node
                try:
                    current_next_node = current_node.next_node
                except AttributeError:
                    exit
        return False

    def __repr__(self) -> str:
        """
        Representation of items in LinkedList object
        Takes O(n) time
        """
        node_list = []
        current_node = self.head
        # loop till next_node doesn't exists
        while current_node:
            if current_node is self.head:
                node_list.append(f"[Head: {current_node.data}]")
            elif current_node.next_node is None:
                node_list.append(f"[Tail: {current_node.data}]")
            else:
                node_list.append(f"[{current_node.data}]")

            current_node = current_node.next_node

        return "->".join(node_list)


l = LinkedList()
l.add(20)
l.add(30)
l.add(40)
l.add(50)

print(l)

print(l.search(20))
print(l.search(80))

l.insert(55, 2)
print(l)
l.insert(65, 2)
print(l)
l.insert(75, 5)
print(l)

l.remove(55)
print(l)
l.remove(20)
print(l)
l.remove()
print(l)