class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        mp = 0

        while r < len(prices):
            mp = max(prices[r] - prices[l], mp)
            if prices[l] > prices[r]:
                l = r
            r += 1
        
        return mp