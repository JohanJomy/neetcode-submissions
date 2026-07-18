class Solution:
    def checkValidString(self, s: str) -> bool:
        leftmin, leftmax = 0, 0

        for i in s:

            # )) ((
            # cannot recover from the first 2 )
            if leftmax < 0:
                return False

            if i == '(':
                leftmax += 1
                leftmin += 1
            elif i == ')':
                leftmax -= 1
                leftmin -= 1
            else:
                leftmin -= 1
                leftmax += 1

            
            leftmin = max(0, leftmin)

        return leftmin <= 0 <= leftmax