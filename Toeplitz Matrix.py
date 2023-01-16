class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        hashmap = {}
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row-col in hashmap:
                    if matrix[row][col] != hashmap[row-col]:
                        return False
                else:
                    hashmap[row-col] = matrix[row][col]

        return True
