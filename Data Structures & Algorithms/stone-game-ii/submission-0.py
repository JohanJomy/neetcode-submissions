class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        dp = {}

        def dfs(alice, i, M):
            if i >= len(piles):
                return 0
            
            if (alice, i, M) in dp:
                return dp[(alice, i, M)]

            sm = 0
            res = 0 if alice else float('inf')
            for j in range(i, min(i+2*M, len(piles))):
                sm += piles[j]
                m = max(M, j-i+1)
                if alice:
                    res = max(res, sm + dfs(not alice, j+1, m))
                else:
                    res = min(res, dfs(not alice, j+1, m))
            
            dp[(alice, i, M)] = res

            return res

        return dfs(True, 0, 1)
