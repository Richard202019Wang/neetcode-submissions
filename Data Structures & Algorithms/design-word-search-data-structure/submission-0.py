class TrieNode:
    def __init__(self):
        self.children = {}
        self.isend = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for s in word:
            if s not in cur.children:
                cur.children[s] = TrieNode()
            cur = cur.children[s]
        cur.isend = True

    def search(self, word: str) -> bool:
        node = [self.root]
        
        for c in word:
            next_nodes = []
            for cur in node:
                if c == '.':
                    next_nodes.extend(cur.children.values())
                else:
                    if c in cur.children:
                        next_nodes.append(cur.children[c])
            if not next_nodes:
                return False 
            
            node = next_nodes
        
        return any(n.isend for n in node)
            
