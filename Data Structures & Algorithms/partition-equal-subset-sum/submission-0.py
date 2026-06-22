class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        dp = set([0])

        target = sum(nums) // 2

        for n in nums:
            new = set()
            for i in dp:
                sm = i + n
                if sm == target:
                    return True
                new.add(sm)
            dp = new.union(dp)

        return target in dp
