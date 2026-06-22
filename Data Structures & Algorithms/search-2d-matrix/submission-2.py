class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
    
        m, n = len(matrix), len(matrix[0])

        # x = i * m + n

        # i = x // m
        # j = x % m

        l, r = 0, m*n - 1

        while l <= r:
            mid = (l + r) // 2

            i = mid // n
            j = mid % n 
            print(mid,m,n, l, r, i, j)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False