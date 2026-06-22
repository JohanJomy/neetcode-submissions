class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqmap = defaultdict(int)

        l = 0
        res = 0
        for r in range(len(s)):
            freqmap[s[r]] += 1

            largestfreq = 0
            for i in freqmap.values():
                largestfreq = max(largestfreq, i)
            
            # length - largestfreq
            while (r-l+1 - largestfreq) > k:
                freqmap[s[l]] -= 1
                l += 1
            print(l, r)
            res = max(res, r-l+1)
        
        return res