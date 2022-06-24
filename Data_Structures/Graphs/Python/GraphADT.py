class Node:
    def __init__(self, value):
        self.value = value

class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacencyList = {}

    def addVertex(self, node):
        self.adjacencyList[node] = []
        self.numberOfNodes += 1
    
    def addEdge(self, node1, node2):
        self.adjacencyList[node1].append(node2)
        self.adjacencyList[node2].append(node1)

    def show_connections(self):
        keys = self.adjacencyList.keys()
        for i in keys:
            nodeConnection = self.adjacencyList[i]
            connections = ""
            for v in nodeConnection:
                connections += str(v) + " "
            
            print(str(i) + " -> " + connections)


# Testing

myGraph = Graph()

myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge('3', '1')
myGraph.addEdge('3', '4')
myGraph.addEdge('4', '2')
myGraph.addEdge('4', '5')
myGraph.addEdge('1', '2')
myGraph.addEdge('1', '0')
myGraph.addEdge('0', '2')
myGraph.addEdge('6', '5')

myGraph.show_connections(); 