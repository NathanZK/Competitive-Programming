class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = [[1 for _ in range(n)] for _ in range(m)]

        for i in range(1, len(path)):
            for j in range(1, len(path[0])):
                path[i][j] = path[i-1][j] + path[i][j-1]

        return path[-1][-1]