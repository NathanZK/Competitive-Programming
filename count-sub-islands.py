class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = [[0 for _ in range(len(grid2[0]))] for _ in range(len(grid2))]
        countInlands = 0

        def inbound(row, col):
            return 0 <= row < len(grid2) and 0 <= col < len(grid2[0])

        def dfs(row, col):
            nonlocal inland

            visited[row][col] = True
            if grid1[row][col] == 0:
                inland = False

            for r, c in directions:
                newRow = row + r
                newCol = col + c

                if inbound(newRow, newCol) and grid2[newRow][newCol] == 1 and not visited[newRow][newCol]:
                    dfs(newRow, newCol)


        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if grid2[row][col] == 1 and not visited[row][col]:
                    inland = True
                    dfs(row, col)
                    if inland:
                        countInlands += 1

        return countInlands