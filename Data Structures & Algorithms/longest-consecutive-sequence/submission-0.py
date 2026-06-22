class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set()

        for i in nums:
            hashmap.add(i)

        largest = 0
        for i in nums:
            ctr = 0
            if i-1 not in hashmap:
                num = i
                while num in hashmap:
                    ctr += 1
                    num = num + 1
                largest = max(largest, ctr)

        return largest