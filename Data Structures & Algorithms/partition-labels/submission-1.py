class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hmap = {}

        for i in range(len(s)):
            hmap[s[i]] = i
        
        res = []

        l, r = 0, 0

        last = 0
        while r < len(s):
            last = max(last, hmap[s[r]])
            if last == r:
                res.append(r-l+1)
                l = r+1
            
            r += 1
        
        return res