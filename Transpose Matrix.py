class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        newMatrix = [[0]*len(matrix) for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                newMatrix[j][i] = matrix[i][j]

        return newMatrix
