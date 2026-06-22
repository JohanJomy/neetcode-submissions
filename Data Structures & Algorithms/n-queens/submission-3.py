class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        # in posistive diag r+c is a constant
        # in negative diag r-c is a constant

        posdiag = set()
        negdiag = set()
        col = set()

        cur = []
        def dfs(r):
            if r == n:
                board = []
                # print(cur)
                for i in cur:
                    board.append('.'*i + 'Q' + '.'*(n-i-1))
                res.append(board)
                return
                    
            for c in range(n):
                # if c in col or (r + c) in posdiag or (r - c) in negdiag:
                #     continue
                if c not in col and (r-c) not in negdiag and (r+c) not in posdiag:
                    
                    col.add(c)
                    negdiag.add(r-c)
                    posdiag.add(r+c)

                    cur.append(c)
                    dfs(r+1)
                    cur.pop()

                    col.remove(c)
                    negdiag.remove(r-c)
                    posdiag.remove(r+c)

        dfs(0)
        return res
