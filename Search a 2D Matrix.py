class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        row = 0
        for r in range(len(matrix)):
            if target >= matrix[r][0]:
                row = r
        
        for c in range(len(matrix[0])):
            if target == matrix[row][c]:
                return True
        
        return False
