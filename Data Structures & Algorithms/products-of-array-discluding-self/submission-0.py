class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1]

        prefix = 1
        for i in range(1, len(nums)):
            prefix *= nums[i-1]
            res.append(prefix)
        
        postfix = 1
        for i in range(len(nums)-2, -2, -1):
            res[i+1] *= postfix 
            postfix  *= nums[i+1]

        return res
