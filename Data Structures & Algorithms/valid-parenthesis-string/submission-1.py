import functools

class Solution:
    def checkValidString(self, s: str) -> bool:
        
        @functools.cache
        def backtrack(i, stack):
            if i == len(s):
                return stack == 0
            
            if stack < 0:
                return False
            
            if s[i] == '(':
                return backtrack(i+1, stack+1)
            
            if s[i] == ')':
                
                return backtrack(i+1, stack-1)
            
            # * = ''
            if backtrack(i+1, stack):
                return True
            
            # * = (
            if backtrack(i+1, stack+1):
                return True
            
            # )
            return backtrack(i+1, stack-1)
        
        return backtrack(0, 0)
            