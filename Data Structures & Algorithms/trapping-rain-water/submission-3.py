class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        sufix = []

        mx = 0
        for i in range(len(height)):
            prefix.append(mx)
            mx = max(mx, height[i])

        mx = 0
        for i in range(len(height)-1, -1, -1):
            sufix.insert(0,mx)
            mx = max(mx, height[i])

        print(prefix, sufix)

        res = 0
        for i in range(len(height)):
            water = min(prefix[i], sufix[i]) - height[i]
            if water > 0:
                res += water
        
        return res