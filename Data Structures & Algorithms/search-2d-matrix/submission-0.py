class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, floor = 0, len(matrix) - 1
        while top <= floor:
            mid_row = (top + floor) // 2
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                floor = mid_row - 1
            else:
                break
        if not top <= floor:
            return False
        l, r = 0, len(matrix[0]) - 1
        target_row = (top + floor) // 2
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[target_row][mid]:
                l = mid + 1
            elif target < matrix[target_row][mid]:
                r = mid - 1
            else:
                return True
        return False