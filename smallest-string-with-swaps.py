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
        sameRep = defaultdict(set)

        for k in self.rep.keys():
            sameRep[self.find(k)].add(k)

        return sameRep

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))
        finalLocation = {i: i for i in range(len(s))}

        for src, des in pairs:
            uf.union(src, des)

        sameRep = uf.sameRep()
        for group in sameRep.values():
            chars = [s[i] for i in group]
            chars.sort()
            sortedGroup = sorted(group)

            for i in range(len(sortedGroup)):
                finalLocation[sortedGroup[i]] = chars[i]

        smallest = []
        for i in range(len(s)):
            smallest.append(finalLocation[i])
            
        return "".join(smallest)