class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        size = len(num1) + len(num2)
        res = [0] * size
        

        for i in range(len(num1)):
            for j in range(len(num2)):

                m = int(num1[len(num1)-i-1]) * int(num2[len(num2) - j - 1])

                new = res[i+j] + m
                if new < 10:
                    res[i+j] = new
                else:
                    res[i+j] = new%10
                    res[i+j+1] += new//10


                        
                    
        
        if res[-1] == 0:
            res = res[:-1]
            return ''.join(map(str, res[::-1]))
        

        return ''.join(map(str, res[::-1]))