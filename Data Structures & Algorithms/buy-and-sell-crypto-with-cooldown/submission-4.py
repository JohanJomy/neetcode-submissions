sys.setrecursionlimit(1000000)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {}
        def dfs(i, bought):
            if i >= len(prices):
                return 0
            
            if (i, bought) in dp:
                return dp[(i, bought)]
            
            if not bought:
                buy = dfs(i+1, True) + (-prices[i])
                skip = dfs(i+1, False)
                dp[(i, bought)] = max(buy, skip)
            
            if bought:
                sell = dfs(i+2, False) + (prices[i])
                skip = dfs(i+1, True)

                dp[(i, bought)] = max(sell, skip)

            return dp[(i, bought)]
        
        return dfs(0, False)