"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        stack = deque([node])
        visit = {}
        visit[node] = Node(node.val)
        while stack:
            cur_node = stack.popleft()
            for neighbor in cur_node.neighbors:
                if neighbor not in visit:
                    visit[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                visit[cur_node].neighbors.append(visit[neighbor])
        return visit[node]

        