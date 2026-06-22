class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS, COLS = len(board), len(board[0])
        visited = set()
        directions = [[-1,0], [1,0], [0,-1], [0,1]]

        def dfs(r, c):
            if (r not in range(ROWS) or
            c not in range(COLS) or
             board[r][c] == 'X' or
             (r,c) in visited):
                return
            
            board[r][c] = 'T'
            visited.add((r,c))

            for dr, dc in directions:   
                ro = r + dr
                co = c + dc
                dfs(ro, co)
        
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS-1)
        
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS-1, c)
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == "T":
                    board[r][c] = 'O'