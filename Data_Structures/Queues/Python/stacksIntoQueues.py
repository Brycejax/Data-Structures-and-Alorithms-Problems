# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a 
# normal queue (push, peek, pop, and empty).

class MyQueue:

    def __init__(self):
        self.length = 0
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.length += 1

    def pop(self) -> int:
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
            
        answer = self.stack2.pop()
        
        for j in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        self.length -= 1
        
        return answer

    def peek(self) -> int:
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
            
        answer = self.stack2[-1]
        
        for j in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return answer

        
    def empty(self) -> bool:
        return self.length == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()