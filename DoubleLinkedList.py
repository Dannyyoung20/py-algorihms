#Node Class

class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.prevNode = None

class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def insertAtStart(self, data):

        newNode = Node(data)
        self.size += 1

        if self.head is None:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def insertAtEnd(self,data):
        self.size += 1
        newNode = Node(data)
        actualNode = self.head

        if self.head is None:
            self.head = newNode

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode
        newNode.prevNode = actualNode

    def size1(self):
        return self.size

    def remove(self, data):
        if self.size is None:
            return

        self.size -= 1

        actualNode = self.head

        while actualNode.data != data:
            actualNode.nextNode.prevNode = actualNode
            actualNode = actualNode.nextNode

        if actualNode.prevNode is not None:
            actualNode.prevNode.nextNode = actualNode.nextNode
            actualNode.nextNode.prevNode = actualNode.prevNode
            actualNode = None
        else:
            actualNode.nextNode.prevNode = actualNode.prevNode
            actualNode = None

    def traverse1(self):
        if self.size is None:
            return

        actualNode = self.head

        while actualNode is not None:
            print('%d' % actualNode.data)
            actualNode = actualNode.nextNode




double_ll = DoubleLinkedList()
double_ll.insertAtStart(20)
double_ll.insertAtStart(12)
double_ll.insertAtEnd(30)
double_ll.traverse1()
double_ll.remove(12)
double_ll.traverse1()
print(double_ll.size1())