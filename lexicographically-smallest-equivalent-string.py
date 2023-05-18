class UnionFind:
    def __init__(self, s1, s2):
        self.rep = {}
        for char in s1:
            self.rep[char] = char

        for char in s2:
            self.rep[char] = char

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

        self.rep[max(xRep, yRep)] = min(xRep, yRep)

    def repExists(self, x):
        return x in self.rep

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind(s1, s2)

        for i in range(len(s1)):
            uf.union(s1[i], s2[i])

        smallest = []
        for char in baseStr:
            if uf.repExists(char):
                smallest.append(uf.representative(char))
            else:
                smallest.append(char)

        return "".join(smallest)