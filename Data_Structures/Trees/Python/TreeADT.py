
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
print()
print("In Order: ")
print(tree.prettyPrintInOrder(tree.root), end="\n")
print("Pre Order: ")
print(tree.prettyPrintPreOrder(tree.root), end="\n")
print("Post Order: ")
print(tree.prettyPrintPostOrder(tree.root), end="\n")

