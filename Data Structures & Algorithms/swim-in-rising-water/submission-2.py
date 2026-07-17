class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)

        visited = {(0, 0)}
        minheap = [(grid[0][0], 0, 0)] #maxheight, row, col

        directions = [(-1,0), (1,0), (0,1), (0, -1)]

        
        while minheap:
            t, r, c = heapq.heappop(minheap)

            if (r, c) == (n-1, n-1):
                return t
            

            for dr, dc in directions:
                row, col = r + dr, c + dc

                if (row, col) not in visited and 0 <= row < n and 0 <= col < n:
                    heapq.heappush(minheap, (max(t, grid[row][col]), row, col))
                    visited.add((row,col))
