class UnionFind:
    def __init__(self):
        self.rep = {chr(i):chr(i) for i in range(97, 123)}
        self.size = {chr(i):0 for i in range(97, 123)}

    def find(self, x):
        if x == self.rep[x]:
            return x
        self.rep[x] = self.find(self.rep[x])
        return self.rep[x]

    def union(self, x, y):
        xRep = self.find(x)
        yRep = self.find(y)

        if xRep != yRep:
            if self.size[xRep] > self.size[yRep]:
                self.rep[yRep] = xRep
            elif self.size[xRep] < self.size[yRep]:
                self.rep[xRep] = yRep
            else:
                self.rep[xRep] = yRep
                self.size[yRep] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()

        for eq in equations:
            if eq[1] == "=":
                uf.union(eq[0], eq[-1])

        for eq in equations:
            if eq[1] == "!" and uf.connected(eq[0], eq[-1]):
                return False

        return True