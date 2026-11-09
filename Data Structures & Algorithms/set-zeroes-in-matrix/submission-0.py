class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows, cols = len(matrix), len(matrix[0])
        
        # 第 1 步：先单独检查第一行和第一列原本有没有 0（只用 2 个布尔变量，O(1) 空间）
        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))
        
        # 第 2 步：遍历除去第一行和第一列的内部区域 (1 ~ rows-1, 1 ~ cols-1)
        # 一旦发现 0，就把对应的“行头”和“列头”标为 0
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        # 第 3 步：根据第一行和第一列的标记，把内部区域对应的位置置 0
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        # 第 4 步：最后根据最开始记下的两个布尔变量，决定要不要把第一行和第一列自己置 0
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0
                
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0