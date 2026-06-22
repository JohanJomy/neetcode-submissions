class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()

        D = [(1,0), (-1,0), (0,1), (0,-1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
                    
        if not fresh:
            return 0
        
        time = 0
        while q:
            time += 1

            for _ in range(len(q)):
                row, col = q.popleft()

                for dr, dc in D:
                    r, c = row+dr, dc+col

                    if (
                        r in range(ROWS) and
                        c in range(COLS) and
                        (r, c) not in visited and
                        grid[r][c] == 1
                    ):
                        fresh -= 1
                        visited.add((r,c))
                        q.append((r,c))
        
        if fresh == 0:
            return time - 1

        return -1

                    