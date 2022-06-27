
class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
        else:
            currNode = self.root
            while True:
                if value < currNode.value:
                    if currNode.left == None:
                        currNode.left = newNode
                        return self
                    currNode = currNode.left
                else:
                    if currNode.right == None:
                        currNode.right = newNode
                        return self
                    currNode = currNode.right
            
    def lookup(self, value):
        if self.root == None:
            return False
        
        currNode = self.root
        while currNode != None:
            if value < currNode.value:
                currNode = currNode.left
            elif value > currNode.value:
                currNode = currNode.right
            elif currNode.value == value:
                return True
            return False

    def remove(self,value):
        if self.root == None:
            return False

        currNode = self.root
        parentNode = None
        while currNode != None:
            if value < currNode.value:
                parentNode = currNode
                currNode = currNode.left
            elif value > currNode.value:
                parentNode = currNode
                currNode = currNode.right
            elif currNode.value == value:
                if currNode.right == None:
                    if parentNode == None:
                        self.root = currNode.left
                    else:
                        if currNode.value < parentNode.value:
                            parentNode.left = currNode.left
                        elif currNode.value > parentNode.value:
                            parentNode.right = currNode.left
                elif currNode.right.left == None:
                    if parentNode == None:
                        self.root = currNode.left
                    else:
                        currNode.right.left = currNode.left
                        if currNode.value < parentNode.value:
                            parentNode.left = currNode.right
                        elif currNode.value > parentNode.value:
                            parentNode.right = currNode.right
                else:
                    leftmost = currNode.right.left
                    leftmostParent = currNode.right
                    while leftmost.left != None:
                        leftmostParent = leftmost
                        leftmost = leftmost.left

                    leftmostParent.left = leftmost.right
                    leftmost.left = currNode.left
                    leftmost.right = currNode.right

                    if parentNode == None:
                        self.root = leftmost
                    else:
                        if currNode.value < parentNode.value:
                            parentNode.left = leftmost
                        elif currNode.value > parentNode.value:
                            parentNode.right = leftmost
        return True
    
    # Impliment BFS for a tree               
    def breadthFirstSearch(self):
        currNode = self.root
        arr = []
        q = []
        q.append(currNode)

        while len(q) > 0:
            currNode = q[0]
            del q[0]
            arr.append(currNode.value)
            if currNode.left:
                q.append(currNode.left)
            if currNode.right:
                q.append(currNode.right)

        return arr

    def breadthFirstSearchRecursive(self, queue, arr):
        if len(queue) == 0:
            return arr

        currnode = queue[0]
        del queue[0]
        arr.append(currnode.value)
        if currnode.left:
            queue.append(currnode.left)
        if currnode.right:
            queue.append(currnode.right)

        return self.breadthFirstSearchRecursive(queue,arr)

    def traverseInOrder(self, node, myList):
        if node.left:
            self.traverseInOrder(node.left, myList)
        
        myList.append(node.value)
    
        if node.right:
            self.traverseInOrder(node.right, myList)

        return myList

    def traversePreOrder(self, node, myList):
        myList.append(node.value)
        
        if node.left:
            self.traversePreOrder(node.left, myList)
        
        if node.right:
            self.traversePreOrder(node.right, myList)

        return myList

    def traversePostOrder(self, node, myList):
        
        if node.left:
            self.traversePreOrder(node.left, myList)
    
        if node.right:
            self.traversePreOrder(node.right, myList)

        myList.append(node.value)
        return myList
        

    def DFSInOrder(self):
        return self.traverseInOrder(self.root, [])

    def DFSPostOrder(self):
        return self.traversePostOrder(self.root, [])

    def DFSPreOrder(self):
        return self.traversePreOrder(self.root, [])

    def prettyPrintInOrder(self, root):
        ans = []
        if root:
            ans = self.prettyPrintInOrder(root.left)
            ans.append(root.value)
            ans = ans + self.prettyPrintInOrder(root.right)
        return ans

    def prettyPrintPreOrder(self, root):
        ans = []
        if root:
            ans.append(root.value)
            ans = ans + self.prettyPrintPreOrder(root.left)
            ans = ans + self.prettyPrintPreOrder(root.right)
        return ans

    def prettyPrintPostOrder(self,root):
        ans = []
        if root:
            ans = self.prettyPrintPostOrder(root.left)
            ans = ans + self.prettyPrintPostOrder(root.right)
            ans.append(root.value)
        return ans
            
# Testing

tree = BinarySearchTree()
tree.insert(15)
tree.insert(20)
tree.insert(10)
tree.insert(65)
tree.insert(76)
tree.insert(87)
tree.insert(2)
tree.insert(3)
tree.insert(14)
# print()
# print("In Order: ")
# print(tree.prettyPrintInOrder(tree.root), end="\n")
# print("Pre Order: ")
# print(tree.prettyPrintPreOrder(tree.root), end="\n")
# print("Post Order: ")
# print(tree.prettyPrintPostOrder(tree.root), end="\n")

# mylist = tree.breadthFirstSearch()
# print(mylist)
# mylistR = tree.breadthFirstSearchRecursive([tree.root], [])
# print(mylistR)

print(tree.traverseInOrder(tree.root, []))
print(tree.traversePreOrder(tree.root, []))
print(tree.traversePostOrder(tree.root, []))
