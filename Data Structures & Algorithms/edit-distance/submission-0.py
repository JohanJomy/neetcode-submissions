class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        matrix = [[-1] * (len(word2) + 1) for _ in range(len(word1)+1)] 

        j = len(word1)

        v = len(word2)
        for i in range(len(word2)+1):
            matrix[j][i] =  v
            v -= 1
        
        j = len(word2)
        v = len(word1)
        for i in range(len(word1)+1):
            matrix[i][j] = v
            v -= 1
        
        
        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    matrix[i][j] = matrix[i+1][j+1]
                else:
                    matrix[i][j] = 1 + min(
                        matrix[i+1][j], # delete
                        matrix[i+1][j+1], # replace
                        matrix[i][j+1] # insert
                    )


        return matrix[0][0]