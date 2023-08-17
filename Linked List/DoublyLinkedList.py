class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

def main():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.append(1)
    doubly_linked_list.append(2)
    doubly_linked_list.append(3)

    print("Forward traversal:")
    doubly_linked_list.display_forward()  # Output: 1 <-> 2 <-> 3 <-> None

    print("Backward traversal:")
    doubly_linked_list.display_backward()  # Output: 3 <-> 2 <-> 1 <-> None


if __name__ == '__main__':
    main()
