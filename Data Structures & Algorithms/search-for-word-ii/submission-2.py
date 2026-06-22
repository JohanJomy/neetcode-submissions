class TriNode:
    def __init__(self):
        self.children = {}
        self.endWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TriNode()

        for word in words:
            cur = root
            for l in word:
                if l not in cur.children:
                    node = TriNode()
                    cur.children[l] = node
                cur = cur.children[l]

            cur.endWord = True

        n = len(board)
        m = len(board[0])

        path = set()
        word = ''
        res = set()

        cur = root
        def dfs(i, j):
            nonlocal cur, word
            if ((i, j) in path or
                i >= n or i < 0 or
                j >= m or j < 0 or board[i][j] not in cur.children):

                # cur = root
                return
            

            l = board[i][j]

            word += l
            
            path.add((i,j))


            if l in cur.children and cur.children[l].endWord:
                res.add(word)

            t = cur
            cur = cur.children[l]

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

            path.remove((i,j))
            word = word[:-1]
            cur = t
        
        for i in range(n):
            for j in range(m):
                dfs(i, j)
            
        return list(res)
            

