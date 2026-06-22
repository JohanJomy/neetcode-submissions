class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            r = self.getrow(board, i, 0)
            print(r)
            if len(r) != len(set(r)):
                return False
        
        for i in range(9):
            c = self.getcol(board, 0, i)
            # print(c)
            if len(c) != len(set(c)):
                return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                b = self.getbox(board, i,j)
                if len(b) != len(set(b)):
                    return False
        
        return True
            
    
    def getrow(self, board, i, j):
        row = []
        for k in range(9):
            if board[i][k] != '.':
                row.append(board[i][k])
        return row
    
    def getcol(self, board, i, j):
        col = []

        for k in range(9):
            if board[k][j] != '.':
                col.append(board[k][j])
        
        return col
    
    def getbox(self, board, i, j):
        box = []

        row_start = (i//3) * 3
        col_start = (j//3) * 3

        for r in range(row_start, row_start+3):
            for c in range(col_start, col_start+3):
                if board[r][c] != '.':
                    box.append(board[r][c])
        
        return box
