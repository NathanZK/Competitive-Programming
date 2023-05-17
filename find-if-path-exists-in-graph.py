class Solution:
    def __init__(self):
        self.size = defaultdict(int)

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

        if xRep != yRep:
            if self.size[xRep] > self.size[yRep]:
                self.rep[yRep] = xRep
                self.size[xRep] += self.size[yRep]
            else:
                self.rep[xRep] = yRep 
                self.size[yRep] += self.size[xRep]


    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.rep = {i:i for i in range(n)}

        if not edges:
            return source == destination

        # for src, des in edges:
        #     self.rep[src] = src
        #     self.rep[des] = des

        for src, des in edges:
            self.union(src, des)


        return self.representative(source) == self.representative(destination)