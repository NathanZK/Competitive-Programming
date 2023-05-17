class UnionFind:
    def __init__(self, size):
        self.rep = {i: i for i in range(1, size+1)}

    def representative(self, x):
        parent = x
        while parent != self.rep[parent]:
            parent = self.rep[parent]

        while x != self.rep[x]:
            self.rep[x] = parent
            x = self.rep[x]

        return parent

    def union(self, x, y):
        xRep = self.representative(x)
        yRep = self.representative(y)

        self.rep[xRep] = yRep

    def connected(self, x, y):
        return self.representative(x) == self.representative(y)


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))

        for src, des in edges:
            if uf.connected(src, des):
                return [src, des]
            uf.union(src, des)