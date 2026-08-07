class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        mx = -31000

        i, j = 0, 0

        n = len(nums)
        while i < n:
            j = i
            sm = nums[i]

            ctr = 1
            while sm > 0 and ctr < n:
                j += 1
                ctr += 1

                mx = max(sm, mx)
                sm += nums[j%n]

            mx = max(sm, mx)
            i += 1

        return mx