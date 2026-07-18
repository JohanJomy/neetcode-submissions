from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # dp = {} # (i, buying): maxProfit

        @cache
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            
            cooldown = dfs(i+1, buying)

            if buying:
                buy = dfs(i+1, False) - prices[i]
                res = max(buy, cooldown)
            
            else:
                sell = dfs(i+2, True) + prices[i]
                res = max(sell, cooldown)
            
            return res
        
        return dfs(0, True)

