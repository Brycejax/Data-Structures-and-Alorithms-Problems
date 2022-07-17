# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxDepthRecursiveDFS(self, root):
        if not root:
            return 0
        
        return 1 + max(self.maxDepthRecursiveDFS(root.left), self.maxDepthRecursiveDFS(root.right))


    def maxDepthBFS(self,root):
        if not root:
            return 0

        level = 0
        q = collections.deque([root])
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return level

    def maxDepthIterativeDFS(self, root):
        if not root:
            return 0
        
        stack = [[root, 1]]
        result = 1
        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return result