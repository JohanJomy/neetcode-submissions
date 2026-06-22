class Solution:
    def countSubstrings(self, s: str) -> int:
        ctr = 0

        for i in range(len(s)):
            
            # odd length 
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ctr += 1
                r += 1
                l -= 1

            # even length 
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ctr += 1
                r += 1
                l -= 1
        
        return ctr