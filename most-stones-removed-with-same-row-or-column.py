class UnionFind:
    def __init__(self, size):
        self.rep = {i: i for i in range(size)}
        self.size = {i: 0 for i in range(size)}
 
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

    def sameRep(self):
        represent = defaultdict(list)

        for k in self.rep.keys():
            represent[self.find(k)].append(k)

        return represent


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind(len(stones))

        for i in range(len(stones)):
            for j in range(i+1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    uf.union(i, j)

        reps = uf.sameRep()
        removeStones = 0
        for group in reps.values():
            removeStones += (len(group) - 1)

        return removeStones