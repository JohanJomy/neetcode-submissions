class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (temp, indx)
        res = [0 for i in range(len(temperatures))]

        for i in range(len(temperatures)):
            temp = temperatures[i]

            while stack and stack[-1][0] < temp:
                t, indx = stack.pop()
                res[indx] = i-indx
                
            # if not stack or stack[-1][0] > i:
            stack.append((temp, i))
            
        print(stack)
        return res
            
                
