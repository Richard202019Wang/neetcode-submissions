class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top, down, l, r = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while l <= r and top <= down:
            for i in range(l, r + 1):
                result.append(matrix[top][i])
            top += 1
            
            for i in range(top, down + 1):
                result.append(matrix[i][r])
            r -= 1

            if not (l <= r and top <= down):
                break
            
            for j in range(r, l - 1, -1):
                result.append(matrix[down][j])
            down -= 1
            
            for i in range(down, top - 1, -1):
                result.append(matrix[i][l])
            l += 1

        return result

        