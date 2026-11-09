class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows, cols = len(matrix), len(matrix[0])
        first_row_0 = False
        first_col_0 = False
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_0 = True
                break
        for i in range(cols):
            if matrix[0][i] == 0:
                first_row_0 = True
                break
        
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if first_row_0:
            for j in range(cols):
                matrix[0][j] = 0
        if first_col_0:
            for j in range(rows):
                matrix[j][0] = 0
