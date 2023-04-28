class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        queue = deque([[[0, 0], 1]])
        directions = [(0,1),(0,-1), (1,0),(-1,0), (1,1),(1,-1),(-1,1), (-1,-1)]
        visited[0][0] = True

        if grid[0][0] == 1:
            return -1

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        while queue:
            curr, path  = queue.popleft()
            if curr == [len(grid)-1, len(grid)-1]:
                return path

            for r, c in directions:
                newRow = curr[0] + r
                newCol = curr[1] + c

                if inbound(newRow, newCol) and not visited[newRow][newCol] and grid[newRow][newCol] == 0:
                    queue.append([[newRow, newCol], path + 1])
                    visited[newRow][newCol] = True

        return -1