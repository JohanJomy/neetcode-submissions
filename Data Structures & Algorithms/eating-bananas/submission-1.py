from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)

        while l<=r:
            mid = (l+r)//2
            t = 0
            for i in piles:
                t += ceil(i/mid)
            
            if t > h:
                l = mid + 1
            else:
                res = min(res, mid)
                r = mid - 1

            
        return res