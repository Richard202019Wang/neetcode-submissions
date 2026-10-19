# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([(root, 0)])
        result = []
        last_d = 0
        last_node = root
        while queue:
            cur_node, depth = queue.popleft()
            if depth != last_d:
                result.append(last_node.val)
                last_d = depth
            last_node = cur_node
            if cur_node.left:
                queue.append((cur_node.left, depth + 1))

            if cur_node.right:
                queue.append((cur_node.right, depth + 1))
        if last_node:
            result.append(last_node.val)
        return result