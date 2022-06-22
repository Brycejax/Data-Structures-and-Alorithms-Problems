
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
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
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1

    def prepend(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def insert(self, index, value):

        if index >= self.length:
            self.append(value)
            return
            
        newNode = Node(value)
        destinationNode = self.traverseToIndex(index-1)
        holdNode = destinationNode.next
        destinationNode.next = newNode
        newNode.next = holdNode
        self.length += 1

    def delete(self, index):

        leaderNode = self.traverseToIndex(index-1)
        delNode = leaderNode.next
        leaderNode.next = delNode.next
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
# Testing

linkedList = LinkedList()
linkedList.append(10)
linkedList.prepend(50)
linkedList.prepend(30)
linkedList.prepend(20)
linkedList.prettyPrint()
linkedList.insert(2, 13)
linkedList.prettyPrint()
linkedList.delete(2)
linkedList.prettyPrint()