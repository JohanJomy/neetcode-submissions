# 2 pointer
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l, r = 0, len(height) - 1

        lmx, rmx = height[l], height[r]
        res = 0
        while l < r:
            if lmx < rmx:
                l += 1
                lmx = max(lmx, height[l])
                res += lmx - height[l] 
                print('l', l, res)
            else:
                r -= 1
                rmx = max(rmx, height[r])
                res += rmx - height[r] 
                print('r', r, res)
        
        return res