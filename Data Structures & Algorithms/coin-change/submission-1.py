class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            if amount in memo:
                return memo[amount]
            
            res = 1 + min(dfs(amount-i) for i in coins)
            memo[amount] = res
            return res

        res = dfs(amount)
        return -1 if res == float('inf') else res
            