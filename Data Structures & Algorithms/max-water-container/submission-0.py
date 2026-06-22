class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            vol = (r-l) * min(heights[l], heights[r])
            mx = max(mx, vol)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return mx