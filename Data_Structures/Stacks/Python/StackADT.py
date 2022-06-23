# Notice: A Stack can be created with either an array or linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.top = newNode
            self.bottom = self.top
        else:
            newNode.next = self.top
            self.top = newNode

        self.length += 1
    
    def pop(self):
        if (self.length == 0):
            return None

        if (self.top == self.bottom):
            self.bottom = None
        
        currTop = self.top
        self.top = self.top.next
        self.length -= 1
        return currTop

    def isEmpty(self):
        return self.length == 0

    def prettyPrint(self):
        temp = self.top
        while temp != None:
            print(temp.value, end="\n")
            temp = temp.next
        print()

class StackArray:
    def __init__(self):
        self.data = []
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self, value):
        if self.length == 0:
            self.data.append(value)
            self.length = 1
            self.top = self.data[self.length-1]
            self.bottom = self.top
            return self

        self.data.append(value)
        self.top = self.data[self.length-1]
        return self

    def pop(self):
        if (self.length == 0):
            return None

        self.data.pop()
        return self.data[self.length-1]

    def isEmpty(self):
        return self.length == 0

    def prettyPrint(self):
        for i in self.data[::-1]:
            print(i)
        print()



# Testing For Linked List Stack
print("\nTESTING FOR STACK LINKED LIST\n")
stackList = Stack()
stackList.push(2)
stackList.push(3)
stackList.push(4)
stackList.push(5)
print("pop= " + str(stackList.peek()))
stackList.pop()
stackList.push(2)
stackList.prettyPrint()

print("\nTESTING FOR STACK ARRAY\n")
stackListarray = StackArray()
stackListarray.push(2)
stackListarray.push(3)
stackListarray.push(4)
stackListarray.push(5)
stackListarray.peek()
print("pop= " + str(stackListarray.pop()))
stackListarray.push(2)
stackListarray.prettyPrint()