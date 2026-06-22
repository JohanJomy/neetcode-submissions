class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cmn, cmx = 1, 1
        res = max(nums)

        for n in nums:
            if n == 0:
                cmn, cmx = 1, 1
                continue

            new = [n, n*cmn, n*cmx]
            cmn = min(new)
            cmx = max(new)

            res = max(cmx, res)

        return res