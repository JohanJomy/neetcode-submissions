class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        
        mx = nums[-1]
        for i in range(n-3, -1, -1):
            # print(nums[i], mx)
            nums[i] = nums[i] + mx
            mx = max(nums[i+1], mx)
        
        print(nums)
        return max(nums[:2])