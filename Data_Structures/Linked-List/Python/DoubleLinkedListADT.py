
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
            self.length = 1
        else:
            newNode.previous = self.tail
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1

    def prepend(self, value):
        newNode = Node(value)
        self.head.previous = newNode
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def insert(self, index, value):

        if index >= self.length:
            self.append(value)
            return
            
        newNode = Node(value)
        destinationNode = self.traverseToIndex(index-1)
        newNode.previous = destinationNode
        holdNode = destinationNode.next
        destinationNode.next = newNode
        newNode.next = holdNode
        self.length += 1

    def delete(self, index):

        leaderNode = self.traverseToIndex(index-1)
        delNode = leaderNode.next
        leaderNode.next = delNode.next
        leaderNode.next.previous = leaderNode
        self.length -= 1
    
    def traverseToIndex(self, index):
        counter = 0
        currentNode = self.head
        while counter < index:
            currentNode = currentNode.next
            counter += 1
        return currentNode

    def prettyPrint(self):
        Node = self.head
        text = ""
        while Node != None:
            text += str(Node.value) + " -> "
            Node = Node.next
        print(text)

    def prettyPrintBackwards(self):
        Node = self.tail
        text = ""
        while Node != None:
            text += str(Node.value) + " -> "
            Node = Node.previous
        print(text)
# Testing

linkedList = DoubleLinkedList()
linkedList.append(10)
linkedList.prepend(50)
linkedList.prepend(30)
linkedList.prepend(20)
linkedList.prettyPrint()
linkedList.insert(2, 13)
linkedList.prettyPrint()
linkedList.delete(2)
linkedList.prettyPrint()
linkedList.prettyPrintBackwards()