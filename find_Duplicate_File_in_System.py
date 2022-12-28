class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        rootHash = {}
        for path in paths:
            path = path.split()
            for i in range(1, len(path)):
                p = path[i].split("txt")
                if rootHash.get(p[-1], 0) != 0:
                    newPath = path[0] + "/" + p[0] + "txt"
                    rootHash[p[-1]].append(newPath)
                else:
                    rootHash[p[-1]] = [path[0] + "/" + p[0] + "txt"]
                    
        res = []
        for val in rootHash.values():
            if len(val) > 1:
                res.append(val)

        return res
