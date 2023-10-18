class UnionFind:

    def __init__(self, s1, s2):
        self.rep = {}
        for ch in s1:
            self.rep[ch] = ch

        for ch in s2:
            self.rep[ch] = ch

    def find(self, x):
        if x == self.rep[x]:
            return x

        self.rep[x] = self.find(self.rep[x])
        return self.rep[x]

    def union(self, x, y):
        xRep = self.find(x)
        yRep = self.find(y)

        self.rep[max(xRep, yRep)] = min(xRep, yRep)

    def repExists(self, x):
        return x in self.rep

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind(s1, s2)

        for i in range(len(s1)):
            uf.union(s1[i], s2[i])

        smallest = []
        for ch in baseStr:
            if uf.repExists(ch):
                smallest.append(uf.find(ch))
            else:
                smallest.append(ch)

        return "".join(smallest)