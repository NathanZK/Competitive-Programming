class UnionFind:
    def __init__(self, size):
        self.rep = {i:i for i in range(1, size+1)}
        self.size = {i: 1 for i in range(1, size+1)}

    def representative(self, x):
        if self.rep[x] == x:
            return x
        parent = self.representative(self.rep[x])
        self.rep[x] = parent

        return parent

    def union(self, x, y):
        xRep = self.representative(x)
        yRep = self.representative(y)

        if xRep != yRep:
            if self.size[xRep] > self.size[yRep]:
                self.rep[yRep] = xRep
                self.size[xRep] += self.size[yRep]
            else:
                self.rep[xRep] = yRep
                self.size[yRep] += self.size[xRep]

    def connected(self, x, y):
        return self.representative(x) == self.representative(y)

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = UnionFind(n)
        minDist = float('inf')

        for src, des, dist in roads:
            uf.union(src, des)

        for src, des, dist in roads:
            if uf.connected(src, 1):
                minDist = min(minDist, dist)

        return minDist