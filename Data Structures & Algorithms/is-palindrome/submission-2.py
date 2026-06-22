class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        s = s.lower()
        # print(s)
        while l < r:
            while not s[l].isalnum() and l < len(s)-1:
                l += 1
            while not s[r].isalnum() and r > 0:
                r -= 1
            # print(l, r)
            if s[l] != s[r] and l < r:
                return False
            
            r -= 1
            l += 1

        return True
            