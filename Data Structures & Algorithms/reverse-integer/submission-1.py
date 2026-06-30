class Solution:
    def reverse(self, x: int) -> int:

        res = 0
        while x:
            res *= 10
            res += int(math.fmod(x, 10))

            x = int(x/10)
        
        if -2147483648 <= res <= 2147483647:
            return res
        return 0  