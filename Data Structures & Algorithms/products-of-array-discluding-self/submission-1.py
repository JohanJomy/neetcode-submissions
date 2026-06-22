class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # using division
        mul = 1
        zctr = 0
        for i in nums:
            if i != 0:
                mul *= i
            else:
                zctr += 1
        
        if zctr > 1:
            return [0] * len(nums)
        
        res = []

        if zctr == 1:
            for i in range(len(nums)):
                if nums[i] != 0:
                    res += [0]
                else:
                    res += [mul]
        else:
            for i in range(len(nums)):
                res += [int(mul * (nums[i] ** -1))]
        
        return res
