class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        directions = [[1,0], [-1, 0], [0,1], [0,-1]]

        def bfs(r, c):
            q = collections.deque()
            visisted = set()

            q.append((r,c))

            distance = 0
            while q:
                distance += 1

                for i in range(len(q)):
                    row, col = q.popleft()

                    for dr, dc in directions:
                        r, c = dr+row, dc+col
                        if (r in range(ROWS) and
                            c in range(COLS) and
                            grid[r][c] > 0 and
                            (r,c) not in visisted
                            and grid[r][c] > distance
                        ):  
                            # print(r,c, distance)
                            # grid[r][c] = min(grid[r][c], distance)
                            grid[r][c] = distance
                            visisted.add((r,c))
                            q.append((r,c))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    bfs(r, c)
        
        