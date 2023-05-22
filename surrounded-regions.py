class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

        def inbound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        def dfs(row, col):
            visited[row][col] = True

            for r, c in directions:
                newRow = row + r
                newCol = col + c

                if inbound(newRow, newCol) and board[newRow][newCol] == "O" and not visited[newRow][newCol]:
                    dfs(newRow, newCol)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if row == len(board) - 1 or row == 0 or col == 0 or col == len(board[0]) - 1:
                    if board[row][col] == "O" and not visited[row][col]:
                        dfs(row, col)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if not visited[row][col]:
                    board[row][col] = "X"

        return board