"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_dict = {None : None}
        cur = head
        while cur:
            copy_dict[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            copy = copy_dict[cur]
            copy.next = copy_dict[cur.next]
            copy.random = copy_dict[cur.random]
            cur = cur.next
        return copy_dict[head]
        
        