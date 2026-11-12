class TreeNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        current_place = self.root
        for w in word:
            if w not in current_place.children:
                current_place.children[w] = TreeNode()
            current_place = current_place.children[w]
        current_place.word = True


    def search(self, word: str) -> bool:
        def dfs(j, root):
            current_place = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in current_place.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                
                else:
                    if c not in current_place.children:
                        return False
                    current_place = current_place.children[c]
            return current_place.word
        
        return dfs(0, self.root)
            
