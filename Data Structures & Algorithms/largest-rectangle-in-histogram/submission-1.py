class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        stack = [] # (ind, h)
        for i, h in enumerate(heights):
            if not stack or stack[-1][1] <= h:
                stack.append((i, h))
            else:
                while stack and stack[-1][1] > h:
                    ind, hght = stack.pop()
                    area = (i - ind) * hght
                    maxArea = max(maxArea, area)

                stack.append((ind, h))
        
        n = len(heights)
        for e in stack:
            i, h = e
            area = (n-i) * h
            maxArea = max(maxArea, area)

        return maxArea



