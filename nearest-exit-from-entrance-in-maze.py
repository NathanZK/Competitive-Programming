class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]

        queue = deque([entrance])
        visited[entrance[0]][entrance[1]] = True
        level = 0

        def inbound(row, col):
            return 0 <= row < len(maze) and 0 <= col < len(maze[0])

        while queue:
            size = len(queue)
            level += 1
            
            for _ in range(size):
                row, col = queue.popleft()

                for r, c in directions:
                    newRow = r + row
                    newCol = c + col

                    if inbound(newRow, newCol) and maze[newRow][newCol] == "." and not visited[newRow][newCol]:
                        if (newRow==len(maze)-1 or newRow==0 or newCol==0 or newCol==len(maze[0]) -1):
                            return level

                        queue.append((newRow,newCol))
                        visited[newRow][newCol] = True

        return -1