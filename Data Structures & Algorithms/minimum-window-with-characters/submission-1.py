class Solution:
    def minWindow(self, s: str, t: str) -> str:
        fm = defaultdict(int)
        for i in t:
            fm[i] += 1
        
        need, have = 0, 0
        currentmap = {}
        for i in fm.keys():
            need += 1
            currentmap[i] = 0
        
        l, r = 0, 0
        res, reslen = '', float('inf')
        while r < len(s):
            if s[r] in currentmap:
                currentmap[s[r]] += 1
                if currentmap[s[r]] == fm[s[r]]:
                    have += 1
            
            while have == need:
                print(l, r)
                if res == '' or reslen > r-l+1:
                    res = s[l:r+1]
                    reslen = r-l+1

                if s[l] in currentmap:
                    currentmap[s[l]] -= 1
                    if currentmap[s[l]] == fm[s[l]] - 1:
                        have -= 1
                
                l += 1

            r += 1
        
        return res
        
        