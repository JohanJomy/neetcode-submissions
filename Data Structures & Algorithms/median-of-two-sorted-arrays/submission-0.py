class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B =  nums1, nums2 

        totl = len(A) + len(B)
        half = totl // 2

        # make a the smaller array for bs
        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A)-1

        while True:
            mid = (l+r) // 2
            bmid = half - mid - 2 # -2 for fixing the indexing of exta +1 and +1 for half and toatl

            AL = A[mid] if mid >= 0 else float('-inf')
            BL = B[bmid] if bmid >= 0 else float('-inf')

            AR = A[mid+1] if mid+1 < len(A) else float('inf')
            BR = B[bmid+1] if bmid+1 < len(B) else float('inf')

            # if AR >= BL and AL <= BR:
            #     break
            if BL > AR:
                l = mid + 1
            elif BR < AL:
                r = mid - 1
            else:
                if totl % 2 == 1:
                    return min(AR, BR)
                else:
                    return (max(AL, BL) + min(AR, BR)) / 2




