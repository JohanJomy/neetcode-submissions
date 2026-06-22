class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        mn = nums[0]
        while l < r:
            mid = (l + r) // 2
            # target in between
            if nums[mid] > nums[r]:
                l = mid + 1
            # target = l or target in [l, mid -1]
            else:
                # mn = min(mn, nums[mid])
                r = mid
        
        return nums[l]
        # return mn