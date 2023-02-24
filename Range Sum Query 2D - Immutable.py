class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

        for r in range(len(matrix)):
            matrix[r].append(0)

        lastrow = [0]*(len(matrix[0])+1)
        matrix.append(lastrow)

        for row in range(len(matrix)-1):
            for col in range(len(matrix[0])-1):
                matrix[row][col] += (matrix[row-1][col] + matrix[row][col-1] - matrix[row-1][col-1])
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        topLeft = self.matrix[row1-1][col1-1]
        topRight = self.matrix[row1-1][col2]
        bottomLeft = self.matrix[row2][col1-1]
        bottomRight = self.matrix[row2][col2]

        return bottomRight - bottomLeft - topRight + topLeft


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
