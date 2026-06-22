class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        mp = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                mp = max(prices[r] - prices[l], mp)

            r += 1
        
        return mp