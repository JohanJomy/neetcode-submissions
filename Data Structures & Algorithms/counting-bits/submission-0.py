class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)

        msd_val = 1
        for i in range(1, n+1):
            if i >= 2 * msd_val:
                msd_val *= 2
            
            dp[i] = 1 + dp[i-msd_val]
        
        return dp