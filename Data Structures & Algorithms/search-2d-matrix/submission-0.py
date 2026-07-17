class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows * cols - 1

        while top <= bottom:

            mid = top + (bottom - top) // 2

            row = mid // cols
            col = mid % cols

            if matrix[row][col] == target:
                return True
            
            elif matrix[row][col] < target:
                top = mid + 1
            else:
                bottom = mid - 1

        return False