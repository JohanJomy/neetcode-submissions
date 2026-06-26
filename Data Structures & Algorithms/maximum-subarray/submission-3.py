class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        l, r = 0, 1

        sm = nums[0]
        mx = nums[0]

        while r < len(nums):
            if sm < 0:
                sm = 0
            sm += nums[r]
            
            # while sm < 0 and l < r:
            #     sm -= nums[l]
            #     l += 1
            r += 1

            mx = max(sm, mx)

        return mx