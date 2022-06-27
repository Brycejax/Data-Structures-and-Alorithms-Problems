## Searching

# Linear Search - O(n)
* searching for a target in a given list/array

# Binary Search - O(logn)
* start in the middle of the list, see if the target is greater than or less than, then split the list
again based on > or < until we find the target

# Graphs and Tree traversals
* Depth First Search - O(n)
* Breadth First Search - O(n)

    DFS - 
        pros: answering the question - Does the path exist?
        cons: Can become slow
    
    BFS - 
        pros: finding the shortest path
        cons: more memory


# Interview questions - determining which searching algorithm to use
* If you know a solution is not far from the root of the tree: BFS

* If the tree is very deep and solutions are rare: BFS

* If the tree is very wide: DFS

* If solutions are frequent but located deep in the tree: DFS

* Determining whether a path exists between two nodes:DFS

* Finding the shortest path: BFS