class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        one, two = 1, 1

        for i in range(n-1):
            t = one + two
            one = two
            two = t
        
        return two