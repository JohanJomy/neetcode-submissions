class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        sm = sum(stones)
        half = sm // 2

        # split into 2 half of aprox equal weight
        # diff btw the 2 halfs in the result

        dp = {}
        def dfs(i, total):
            if i == len(stones) or total >= half:
                return abs(total - (sm - total))
            
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = min(dfs(i+1, total + stones[i]), dfs(i+1, total))

            return dp[(i, total)]
        
        return dfs(0, 0)