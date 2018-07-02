# Node Class
class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList:

    def __init__(self):
        self.size = 0
        self.head = None

    # Insert a new item in the Linked List
    def insertAtStart(self, data):
        self.size += 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    # Get the linked list size - Faster O(1)
    def size1(self):
        return self.size

    # Another way of implementing the size but slower O(N)
    def size2(self):
        actualNode = self.head
        size = 0

        while actualNode is not None:
            size += 1
            actualNode = actualNode.nextNode

        return size

    # Insert list at the end
    def insertAtEnd(self, data):
        self.size += 1

        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    # Display All Lists
    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print("%d "% actualNode.data)
            actualNode = actualNode.nextNode

    # Delete a list item
    def remove(self, data):
        self.size -= 1

        if self.head is None:
            return

        currentNode = self.head
        previousNode = None

        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode

        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode
