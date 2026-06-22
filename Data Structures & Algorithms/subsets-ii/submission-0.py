class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        def dfs(i, cur):
            if i >= n:
                res.append(cur)
                return
            
            dfs(i+1, cur+[nums[i]])

            i += 1
            while i < n and nums[i] == nums[i-1]:
                i += 1

            dfs(i, cur)
        
        dfs(0, [])
        return res