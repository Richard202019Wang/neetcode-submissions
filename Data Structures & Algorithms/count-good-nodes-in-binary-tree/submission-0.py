# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, root.val)]
        result = 0
        while stack:
            cur_node, max_node = stack.pop()
            if cur_node.val >= max_node:
                result += 1
                max_node = cur_node.val
            if cur_node.left:
                stack.append((cur_node.left, max_node))
            if cur_node.right:
                stack.append((cur_node.right, max_node))
        return result
            