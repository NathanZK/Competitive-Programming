class Solution:
    def printVertically(self, s: str) -> List[str]:
        inp = s.split()
        max_ = len(max(inp, key = len))
        res = [[] for i in range(max_)]

        for i in range(len(inp)):
            for j in range(max_):
                if j < len(inp[i]):
                    res[j].append(inp[i][j])
                else:
                    res[j].append(" ")

        for ind in range(len(res)):
            res[ind] = "".join(res[ind])
            res[ind] = res[ind].rstrip()

        return res
