class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat) - 1
        n = len(mat[0]) - 1
        length = max(len(mat), len(mat[0]))

        res = []
        ind = 0
        while ind < 2*length - 1:
            if ind % 2 == 0:
                i = min(m, ind)
                j = ind - i
                while i >= 0 and j <= n:
                    res.append(mat[i][j])
                    i -= 1
                    j += 1
            else:
                j = min(n, ind)
                i = ind - j
                while j >= 0 and i <= m:
                    res.append(mat[i][j])
                    j -= 1
                    i += 1
            ind += 1

        return res
        
