class Solution:

    def encode(self, strs: List[str]) -> str:

        new = ""
        for i in strs:
            new += str(len(i)) + "#" + i
        
        return new

    def decode(self, s: str) -> List[str]:

        
        i = 0
        strs = []

        while i < len(s):
            num = ''
            while s[i] != '#':
                num += s[i]
                i += 1
            num = int(num)
            i += 1
            
            strs.append(s[i:i+num])

            i += num

        return strs