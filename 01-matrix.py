class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        distances = [[-1 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        queue = deque()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    queue.append([[row, col], 0])
                    distances[row][col] = 0

        def inbound(row, col):
            return 0 <= row < len(mat) and 0 <= col < len(mat[0])

        while queue:
            curr, dist = queue.popleft()

            for r, c in directions:
                newRow = curr[0] + r
                newCol = curr[1] + c

                if inbound(newRow, newCol) and mat[newRow][newCol] != 0 and distances[newRow][newCol] == -1:
                    queue.append([[newRow, newCol], dist + 1])
                    distances[newRow][newCol] = dist + 1

        return distances