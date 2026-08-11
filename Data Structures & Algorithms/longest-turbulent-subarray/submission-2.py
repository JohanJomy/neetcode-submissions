class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        res = 0
        ctr = 0

        sign = -1
        for i in range(len(arr)-1):

            if arr[i] < arr[i+1]:
                ctr = ctr + 1 if sign == 0 else 1
                sign = 1
            elif arr[i] > arr[i+1]:
                ctr = ctr + 1 if sign == 1 else 1
                sign = 0
            else:
                ctr = 0
                sign = -1
            
            res = max(res, ctr)

        return res + 1