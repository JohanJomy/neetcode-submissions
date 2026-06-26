class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        
        a = self.myPow(x, abs(n)//2)
        
        if n > 0:
            if n%2:
                return a * a * x
            
            return a * a
        
        if n%2:
            return 1/(a*a*x)
        
        return 1/(a*a)
        