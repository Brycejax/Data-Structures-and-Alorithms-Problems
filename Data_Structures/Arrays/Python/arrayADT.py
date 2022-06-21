class MyArray:
    def __init__(self):
        self.length = 0
        self.data = []

    def get(self, index):
        return self.data[index]
        
    def push(self, item):
        self.data.append(item)
        self.length += 1

    def pop(self):
        self.length -= 1
        return self.data.pop()

    def delete(self, index):
        self.data.remove(self.get(index))
        self.length -= 1
    
    def prettyPrint(self):
        for i in self.data:
            print(i + "\n")
    

#testing

newArray = MyArray()
newArray.push('hi')
newArray.push('my')
newArray.push('name')
newArray.push('is')
newArray.push('Bryce')

newArray.prettyPrint()

newArray.pop()
newArray.pop()

newArray.prettyPrint()

newArray.push('ist')
newArray.push('not')
newArray.push('Bruce')

newArray.prettyPrint()

newArray.delete(0)

newArray.prettyPrint()