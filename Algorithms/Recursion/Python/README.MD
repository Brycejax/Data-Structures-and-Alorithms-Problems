## Steps and rules of Recursion

1.) Identify a base case
2.) Identify the recursive case
3.) work your way down to the answer
    - typically has a return on the base case, else it returns the function with altered    
    params.

* Anything you can do with recursion, you can also do iteratively.
* Although recursion can keep your code dry, it creates a large stack
* Time complexity is greater than the iterative approach (O(2^n) for fibonnaci recursive approach)

## When should we use recursion?
 * maybe in BFS + DFS (Searching)
 * There are also some sorting in which recursion is prefered

## When to consider it?
 * Every time you are using a tree or converting something into a tree, consider recursion
 * Divide and Conquer using recursion

## Specific Examples
 * Merge Sort
 * Quick Sort
 * Tree Traversal
 * Graph Traversal
