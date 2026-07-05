class Solution:
    # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        t, b = 0, len(matrix)-1
        l, r = 0, len(matrix[0])-1

        res = []
        while l <= r  and t <= b:
            # print("L R")
            for i in range(l, r+1):
                # print(i)
                res.append(matrix[t][i])
            t += 1
            # print("T B")
            for i in range(t, b+1):
                # print(i)
                res.append(matrix[i][r])
            r -= 1

            if l > r or t > b:
                break

            # print("R L")
            for i in range(r, l-1, -1):
                # print(i)
                res.append(matrix[b][i])
            b -= 1
            # print("B T")
            for i in range(b, t-1, -1):
                # print(i)
                res.append(matrix[i][l])
            
            l += 1
        
        return res