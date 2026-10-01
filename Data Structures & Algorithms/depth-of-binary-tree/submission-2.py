# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        res = 0
        while stack:
            node = stack.pop()
            n, depth = node
            
            if n:
                res = max(res, depth)
                stack.append((n.left, depth + 1))
                stack.append((n.right, depth + 1))
        return res
        # if not root:
        #     return 0

            
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))