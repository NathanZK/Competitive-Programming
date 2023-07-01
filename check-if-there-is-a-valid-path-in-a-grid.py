class UnionFind:
    def __init__(self, grid):
        self.rep = {}

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                self.rep[(row, col)] = (row, col)

    def find(self, x):
        parent = x
        while parent != self.rep[parent]:
            parent = self.rep[parent]

        while x != self.rep[x]:
            self.rep[x] = parent
            x = self.rep[x]

        return parent
    
    def union(self, x, y):
        xRep = self.find(x)
        yRep = self.find(y)

        self.rep[xRep] = yRep

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

    def printRep(self):
        return self.rep

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        uf = UnionFind(grid)
        rowLen = len(grid)
        colLen = len(grid[0])

        for row in range(rowLen):
            for col in range(colLen):
                if grid[row][col] == 1 or grid[row][col] == 4 or grid[row][col] == 6:
                    if col+1 < colLen and (grid[row][col+1] == 1 or grid[row][col+1] == 3 or grid[row][col+1] == 5):
                        uf.union((row,col), (row, col+1))
                if grid[row][col] == 2 or grid[row][col] == 3 or grid[row][col] == 4:
                    if row+1 < rowLen and (grid[row+1][col] == 5 or grid[row+1][col] == 6 or grid[row+1][col] == 2):
                        uf.union((row, col), (row+1, col))
    
        return uf.isConnected((0,0),(rowLen-1,colLen-1))