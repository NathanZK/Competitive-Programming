class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = self.traverse(board, 3, 3, 3)
        rows = self.traverse(board, 1, 9, 1)
        columns = self.traverse(board, 9, 1, 1)
        return squares and rows and columns

    def traverse(self, board, dimH, dimV, stride):
        r_range = (9 - dimH) // stride + 1
        c_range = (9 - dimV) // stride + 1
        for r in range(r_range):
            for c in range(c_range):
                row , col = r*stride, c*stride
                count = set()
                for i in range(row, row+dimH):
                    for j in range(col, col+dimV):
                        if board[i][j] in count:
                            return False
                        elif (board[i][j]).isdigit():
                            count.add(board[i][j])

        return True
                
