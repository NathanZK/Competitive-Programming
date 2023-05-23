class UnionFind:
    def __init__(self):
        self.rep = {}
        self.size = defaultdict(int)
 
    def find(self, x):
        if x == self.rep[x]:
            return x
        self.rep[x] = self.find(self.rep[x])
        return self.rep[x]
 
    def union(self, x, y):
        if x not in self.rep:
            self.rep[x] = x
        if y not in self.rep:
            self.rep[y] = y

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
        representatives = defaultdict(set)

        for key in self.rep.keys():
            representatives[self.find(key)].add(key)

        return representatives

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        emailName = {}

        for account in accounts:
            for i in range(1, len(account)):
                uf.union(account[1], account[i])
                emailName[account[i]] = account[0]

        reps = uf.sameRep()
        totalAccounts = []
        for group in reps.values():
            sortedGroup = sorted(group)

            totalAcc = [emailName[sortedGroup[0]]]
            totalAcc += sortedGroup
            totalAccounts.append(totalAcc)
            
        return totalAccounts