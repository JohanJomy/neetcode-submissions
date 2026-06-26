class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        sm = 0
        mx = nums[0]

        for n in nums:
            if sm < 0:
                sm = 0

            sm += n

            mx = max(sm, mx)

        return mx