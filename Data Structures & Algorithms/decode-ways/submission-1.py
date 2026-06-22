class Solution:
    def numDecodings(self, s: str) -> int:
        # res = 0

        memo = {}

        def dp(i):
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0 

            if i in memo:
                return memo[i]
            
            res = dp(i+1)

            if i < len(s) - 1 and (s[i] == '1' or s[i] == '2' and s[i+1] in '0123456'):
                res += dp(i+2)
            
            memo[i] = res

            return res
        
        return dp(0)