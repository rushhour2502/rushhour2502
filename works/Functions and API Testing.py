# Node class
class Node:
    def __init__(self, data):
        self.data = data  # store data
        self.next = None  # pointer to next node


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None  # first node (head)

    # Insert new node at the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:  # if list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # move to the last node
            current = current.next
        current.next = new_node  # link last node to new node

    # Print all nodes
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

ll.display()  # Output: 10 -> 20 -> 30 -> None


def grok():
    print(" this ia an example of a called function")

grok()
