class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        directions = [(1,1), (1,-1), (1, 0)]
        mat = [[float('inf') for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
 
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == 0:
                    mat[i][j] = matrix[i][j]

        for row in range(len(matrix)-1):
            for col in range(len(matrix[0])):
                for r, c in directions:
                    newRow = row + r
                    newCol = col + c

                    if self.bound(newRow, newCol, matrix):
                        mat[newRow][newCol] = min(mat[newRow][newCol], mat[row][col] + matrix[newRow][newCol])

        return min(mat[len(mat)-1])
                
    def bound(self, row, col, matrix):
        return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])
        
