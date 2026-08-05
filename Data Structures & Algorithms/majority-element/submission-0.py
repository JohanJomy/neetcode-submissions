class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = {}

        mx = 0
        res = 0

        for n in nums:
            hmap[n] = hmap.get(n, 0) + 1

            if mx < hmap[n]:
                mx = hmap[n]
                res = n
        
        return res