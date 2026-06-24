class Solution:
    def __init__(self):
        self.hset = set()

    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        
        res = 0
        for d in str(n):
            res += int(d) ** 2
        
        if res in self.hset:
            return False

        # print(res)
        
        self.hset.add(res)
        return self.isHappy(res)
