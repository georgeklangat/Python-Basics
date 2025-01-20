class Node:
    def __init__(self, data, next=None):
        self.data = data  # This is the value the node holds
        self.next = next  # This points to the next node in the list


class LinkedList:
    def __init__(self):
        self.head = None  # this is the starting point of the list

    def add_at_end(self, data):
        new_node = Node(data)  # creating a new node with the given data
        if self.head is None:  # if the list is empty, set the new node at the end
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" ->")
            current = current.next
        print("None")


if __name__ == "__main__":
    llist = LinkedList()
    llist.add_at_end(1)
    llist.add_at_end(2)
    llist.add_at_end(3)
    llist.add_at_end(4)

    print("Original linked list")
    llist.printList()

    print("Linked list  after insertion")
    llist.add_at_end(5)
    llist.printList()
