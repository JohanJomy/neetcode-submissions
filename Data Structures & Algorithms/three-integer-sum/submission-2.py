class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums) - 1

            target = -nums[i]
            while l < r:
                sm = nums[l] + nums[r]
                if sm == target:
                    if [nums[l], nums[r], nums[i]] not in res:
                        res.append([nums[l], nums[r], nums[i]]) 
                    l += 1
                
                if sm > target:
                    r -= 1
                
                if sm < target:
                    l += 1
        
        return res

