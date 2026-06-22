class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        candidates = sorted(candidates)
        print(candidates)
        def dfs(i, cur, sm):
            if sm == target:
                res.append(cur.copy())
                return
            
            if sm > target or i == n:
                return


            dfs(i + 1, cur + [candidates[i]], sm + candidates[i])

            i += 1
            while i < n and candidates[i] == candidates[i-1]:
                i += 1
            
            if i == n: return
            dfs(i, cur, sm)

        dfs(0, [], 0)
        return res