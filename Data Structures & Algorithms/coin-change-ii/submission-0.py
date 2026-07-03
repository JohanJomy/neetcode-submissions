class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = defaultdict(int)

        def dfs(amount, i):
            if amount == 0:
                return 1
            if amount < 0:
                return 0
            
            if (amount, i) in dp:
                return dp[(amount, i)]
            
            sm = 0
            for j in range(i, len(coins)):
                sm += dfs(amount-coins[j], j)
                # print('dp', dp[amount])
 
            dp[(amount, i)] = sm
            return dp[(amount, i)]
        
        res = dfs(amount, 0)
        return res