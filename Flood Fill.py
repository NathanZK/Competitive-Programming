class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(1,0), (-1,0), (0, 1), (0,-1)]
        visited = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]

        def inbound(row, col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])

        def dfs(row, col, start):
            visited[row][col] = True

            for r, c in directions:
                newRow = row + r
                newCol = col + c

                if inbound(newRow, newCol) and not visited[newRow][newCol]:
                    if image[newRow][newCol] == start:
                        image[newRow][newCol] = color
                        dfs(newRow, newCol, start)

        dfs(sr, sc, image[sr][sc])
        image[sr][sc] = color

        return image
