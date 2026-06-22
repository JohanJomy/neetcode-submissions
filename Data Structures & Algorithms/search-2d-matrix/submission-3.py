class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # find row
        l, r = 0, m - 1
        while l <= r:
            mid = (l+r)//2
            if matrix[mid][-1] < target:
                l = mid + 1
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                break
        
        if l > r:
            return False
        
        row = mid
        l, r = 0, n - 1

        while l <= r:
            mid = (l+r)//2

            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
        
        return False