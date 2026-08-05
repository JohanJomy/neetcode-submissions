class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = [0]*3

        for i in nums:
            l[i] += 1
        
        k = 0
        for i, n in enumerate(l):
            for _ in range(n):
                nums[k] = i
                k += 1
