class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rowL, colL = len(mat), 
        flatten = [0 for _ in range(len(mat)* len(mat[0]))]
        if r * c != len(flatten):
            return mat

        ind = 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                flatten[ind] = mat[row][col]
                ind += 1

        reshaped = [[0 for i in range(c)] for j in range(r)]
        for i in range(len(flatten)):
            row, col = i // c, i % c
            reshaped[row][col] = flatten[i]
        
        return reshaped

