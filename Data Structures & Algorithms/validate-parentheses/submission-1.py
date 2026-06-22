class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {'[':']', '{':'}', '(':')'}
        start = ['[', '{', '(']

        for i in s:
            if i in start:
                stack += [hmap[i]]
            else:
                if len(stack) == 0:
                    return False
                elif stack.pop() != i:
                    return False
        
        
        if len(stack) == 0:
            return True
        return False