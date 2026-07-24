class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {'[':']', '{':'}', '(':')'}

        for i in s:
            if i in hmap:
                stack += [hmap[i]]
            else:
                if len(stack) == 0:
                    return False
                elif stack.pop() != i:
                    return False
        
        
        if len(stack) == 0:
            return True
        return False