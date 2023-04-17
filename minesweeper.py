class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,-1),(-1,1),(1,1), (-1,-1)]

        def inbound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        def dfs(row, col):
            if board[row][col] == 'M':
                board[row][col] = "X"
                return

            adjacentMines = 0
            for r, c in directions:
                newRow = row + r
                newCol = col + c

                if inbound(newRow, newCol) and board[newRow][newCol] == "M":
                    adjacentMines += 1

            if adjacentMines > 0:
                board[row][col] = str(adjacentMines)
                return
            
            board[row][col] = "B"
            for r, c in directions:
                newRow = row + r
                newCol = col + c

                if inbound(newRow, newCol) and board[newRow][newCol] != "B":
                    dfs(newRow, newCol)

        dfs(click[0], click[1])
        return board