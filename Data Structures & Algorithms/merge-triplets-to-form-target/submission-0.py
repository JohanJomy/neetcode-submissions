class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        r1, r2, r3 = 1, 1, 1

        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                r1 = max(a, r1)
                r2 = max(b, r2)
                r3 = max(c, r3)
        
        if [r1, r2, r3] == target:
            return True
        
        return False