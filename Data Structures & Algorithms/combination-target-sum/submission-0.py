class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n = len(nums)
        res = []
        
        subset = []
        sm = 0

        def dfs(i):
            nonlocal sm
            if sm == target:
                res.append(subset.copy())
            
            if sm >= target or i >= n:
                return
            
            # include ith elem
            sm += nums[i]
            subset.append(nums[i])

            #includnig the ith elem again
            dfs(i)

            #without ith elem
            sm -= nums[i]
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res

