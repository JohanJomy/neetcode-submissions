class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mn, mx = 1, 1
        res = float('-inf')

        for n in nums:
            if n == 0:
                mn, mx = 1, 1
                res = max(0, res)
            else:
                new = [n, n*mn, n*mx]
                mn = min(new)
                mx = max(new)
                res = max(mx, res)

        return res