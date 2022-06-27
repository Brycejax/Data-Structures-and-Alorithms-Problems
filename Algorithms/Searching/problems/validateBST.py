# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# This requires the creation of BFS or DFS - here i will impliment using BFS
# in BFS, we need a queue data structure.
# in DPF we either need stack or simply recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

def isValidBST(root):
 
    q = collections.deque()
    q.append(root, float("-inf"), float("inf"))

    while q:
        currNode, min_val, max_val = q.popleft()
        if currNode:
            if min_val >= currNode.val or currNode.val >= max_val:
                return False
            if currNode.left:
                q.append(currNode.left, min_val, currNode.val)
            
            if currNode.right:
                q.append(currNode.right, currNode.val, max_val)
    return True

# Success
# Details 
# Runtime: 115 ms, faster than 5.22% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.2 MB, less than 95.46% of Python3 online submissions for Validate Binary Search Tree.