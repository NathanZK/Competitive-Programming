class Solution:
    def __init__(self):
        self.rep = defaultdict(str)

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

        self.rep[yRep] = xRep

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if not edges:
            return source == destination

        for src, des in edges:
            self.rep[src] = src
            self.rep[des] = des

        for src, des in edges:
            self.union(src, des)


        return self.representative(source) == self.representative(destination)