class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        delete = 0
        for i in range(len(strs[0])):
            col = []
            for j in range(len(strs)):
                col.append(strs[j][i])
            if col != sorted(col):
                delete += 1

        return delete
