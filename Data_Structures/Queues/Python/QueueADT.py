from urllib.parse import _NetlocResultMixinBytes


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first.value

    def enqueue(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode

        self.length += 1
        return self

    def dequeue(self):
        if self.length == 0:
            return None
        if self.first == self.last:
            self.last = None
        
        self.first = self.first.next
        self.length -= 1
        return self

    def isEmpty(self):
        return self.length == 0

    def prettyPrint(self):
        currNode = self.first
        while currNode != None:
            print(currNode.value, end=" -> ")
            currNode = currNode.next
        print()


# Testing 

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.prettyPrint()
q.dequeue()
q.prettyPrint()
