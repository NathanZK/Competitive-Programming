class UnionFind:
    def __init__(self, grid):
        self.rep = {(-1,-1):(-1,-1), (len(grid),len(grid[0])): (len(grid),len(grid[0]))}
        self.rank = {(-1,-1):1, (len(grid),len(grid[0])): 1}
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                self.rep[(row,col)] = (row, col)
                self.rank[(row,col)] = 1

    def find(self, x):
        if x == self.rep[x]:
            return x
        self.rep[x] = self.find(self.rep[x])
        return self.rep[x]

    def union(self, x, y):
        repX = self.find(x)
        repY = self.find(y)
        if repX != repY:
            if self.rank[repX] > self.rank[repY]:
                self.rep[repY] = repX
            elif self.rank[repX] < self.rank[repY]:
                self.rep[repX] = repY
            else:
                self.rep[repY] = repX
                self.rank[repX] += 1

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def inbound(self, r, c, row, col):
        return 0 <= r < row and 0 <= c < col

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        grid = [[1 for _ in range(col)] for _ in range(row)]
        directions = [(0, 1), (0,-1), (1,0), (-1,0)]
        uf = UnionFind(grid)
        
        cells = cells[::-1]
        for day in range(len(cells)):
            ro, co = cells[day]
            r, c = ro -1 , co - 1
            grid[r][c] = 0
            if r == 0:
                uf.union((r,c),(-1,-1))
            elif r == row - 1:
                uf.union((r,c), (row,col))
            for i, j in directions:
                newRow = r + i
                newCol = c + j
                if self.inbound(newRow, newCol, row, col) and grid[newRow][newCol] == 0:
                    uf.union((r,c),(newRow, newCol))
            
            if uf.isConnected((-1,-1), (row, col)):
                return len(cells) - day- 1