class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        return max(nums[0], self.helper(nums[:n-1]), self.helper(nums[1:n]))

        # return self.helper(nums)

    def helper(self, nums):

        rob1, rob2 = 0, 0

        # rob1, rob2, 2, 9, 8, 3, 6
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        
        return max(rob1, rob2)