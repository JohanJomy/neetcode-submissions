class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        
        l, r = 0, len(matrix) - 1


        while l<r:
            for i in range(r-l):
                t, b = l, r

                # topleft = matrix[t][l]
                topleft = matrix[t][l+i]

                # matrix[t][l] = matrix[b][l]
                matrix[t][l+i] = matrix[b-i][l]

                # matrix[b][l] = matrix[b][r]
                matrix[b-i][l] = matrix[b][r-i]

                # matrix[b][r] = matrix[t][r]
                matrix[b][r-i] = matrix[t+i][r]

                # matrix[t][r] = topleft
                matrix[t+i][r] = topleft
            
            l += 1
            r -= 1