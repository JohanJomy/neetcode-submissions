class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483647

        res = 0

        while x:
            d = int(math.fmod(x, 10))
            x = int(x/10)

            res *= 10
            res += d
        
        if MIN <= res <= MAX:
            return res
        return 0  