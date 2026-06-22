class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(i, cur, sm):
            if sm == target:
                res.append(cur.copy())
                return
            if sm > target or i == n:
                return
            
            dfs(i, cur + [nums[i]], sm + nums[i])
            dfs(i + 1, cur, sm)

        dfs(0, [], 0)
        return res