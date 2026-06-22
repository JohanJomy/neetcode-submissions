class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqmap = defaultdict(int)

        for i in s1:
            freqmap[i] += 1
        
        l = 0
        r = len(s1) - 1

        if len(s2) < len(s1):
            return False

        fm2 = defaultdict(int)
        for i in range(0, r+1):
            if s2[i] in freqmap:
                fm2[s2[i]] += 1

        if freqmap == fm2:
            return True

        while r < len(s2) - 1:
            if s2[l] in fm2:
                fm2[s2[l]] -= 1
            l += 1
            r += 1

            if s2[r] in freqmap:
                fm2[s2[r]] += 1


            if freqmap == fm2:
                return True


        return False

