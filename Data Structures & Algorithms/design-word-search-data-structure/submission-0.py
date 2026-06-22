class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        
        cur.end = True

    def search(self, word: str) -> bool:

        def dfs(word, cur):
            if not word:
                return cur.end
            
            if word[0] == '.':
                if not cur.children:
                    return False

                for c in cur.children:
                    r = dfs(word[1:], cur.children[c])
                    if r:
                        return True
                return False
            
            if word[0] not in cur.children:
                return False
            
            return dfs(word[1:], cur.children[word[0]]) 
        
        return dfs(word, self.root)
