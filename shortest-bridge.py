class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        queue = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    queue.append((row, col))
                    visited.add((row,col))
                    break

            if len(queue) > 0:
                break

        while queue:
            row, col = queue.popleft()

            for r, c in directions:
                newRow = row + r
                newCol = col + c

                if self.inbound(newRow, newCol, grid) and grid[newRow][newCol] == 1 and (newRow,newCol) not in visited:
                    queue.append((newRow, newCol))
                    visited.add((newRow, newCol))

        queue = deque(visited)
        level = 0

        while queue:
            size = len(queue)
    
            for _ in range(size):
                row, col = queue.popleft()
                
                for r, c in directions:
                    newRow = row + r
                    newCol = col + c

                    if self.inbound(newRow, newCol, grid) and (newRow,newCol) not in visited:
                        if grid[newRow][newCol] == 1:
                            return level
                        else:
                            queue.append((newRow, newCol))
                            visited.add((newRow, newCol))

            level += 1

        return 0

    def inbound(self, row, col, grid):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])