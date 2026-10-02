# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        stack = deque([(root, 0)])
        layer_dict = defaultdict(list)
        while stack:
            node = stack.popleft()
            layer_dict[node[1]].append(node[0].val)
            if node[0].left:
                stack.append((node[0].left, node[1] + 1))
            if node[0].right:
                stack.append((node[0].right, node[1] + 1))
        for vals in layer_dict.values():
            result.append(vals)
        return result

        
        