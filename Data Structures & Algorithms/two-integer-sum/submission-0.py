class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, e in enumerate(nums):
            if target-e in hashmap:
                return [hashmap[target-e], i]
            
            hashmap[e] = i
            