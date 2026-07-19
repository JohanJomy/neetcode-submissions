class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        # we use the first row to check if the col should be 0
        # we use the first col to check if the row should be 0
        # since (0,0) overlaps
        r1 = 1 # this for row 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if matrix[i][j] == 0:
                    if i == 0:
                        r1 = 0
                    else:
                        matrix[i][0] = 0
                    
                    matrix[0][j] = 0
        
        # skip the stored values, process them at the end
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                # if i == 0 and r1 == 0:
                #     matrix[i][j] = 0
                
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for r in range(len(matrix)):
                matrix[r][0] = 0
        
        if r1 == 0:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0


