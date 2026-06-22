class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, r = 0, 0

        chars = set()
        mx = 0

        while r < len(s):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1

            # if s[r] not in chars:
            chars.add(s[r])
            mx = max(r - l + 1, mx)

            r += 1
        
        return mx