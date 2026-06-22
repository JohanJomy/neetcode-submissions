class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        sm = numbers[l] + numbers[r]
        while (sm != target):
            if sm > target:
                r -= 1
            
            if sm < target:
                l += 1
            
            sm = numbers[l] + numbers[r]
        
        return [l+1, r+1]