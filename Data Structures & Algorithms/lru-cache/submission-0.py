class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}
        self.l, self.r = Node(0, 0), Node(0, 0)
        self.l.next, self.r.prev = self.r, self.l
    
    def remove(self, node):
        pre, nxt = node.prev, node.next 
        pre.next, nxt.prev = nxt, pre
    
    def insert(self, node):
        pre, nxt = self.r.prev, self.r
        pre.next = nxt.prev = node
        node.prev = pre
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.nodes:
            self.remove(self.nodes[key])
            self.insert(self.nodes[key])
            return self.nodes[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.remove(self.nodes[key])
        new_node = Node(key, value)
        self.nodes[key] = new_node
        self.insert(new_node)
        if len(self.nodes) > self.capacity:
            node = self.l.next
            self.remove(node)
            del self.nodes[node.key]
        
