class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        directions = [(0,1), (0,-1), (1, 0), (-1,0)]

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def dfs(row, col):
            nonlocal area

            visited[row][col] = True
            for r, c in directions:
                newRow = row + r
                newCol = col + c

                if inbound(newRow, newCol) and not visited[newRow][newCol] and grid[newRow][newCol] == 1:
                    area += 1
                    dfs(newRow, newCol)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and not visited[row][col]:
                    area = 1
                    dfs(row, col)
                    maxArea = max(maxArea, area)

        return maxArea
