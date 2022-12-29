class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row = []
        col = []
        diff = grid.copy()

        for i in range(len(grid)):
            rowCnt = {}
            for j in range(len(grid[i])):
                rowCnt[grid[i][j]] = rowCnt.get(grid[i][j], 0) + 1
            row.append(rowCnt)
            
        for i in range(len(grid[0])):
            colCnt = {}
            for j in range(len(grid)):
                colCnt[grid[j][i]] = colCnt.get(grid[j][i], 0) + 1
            col.append(colCnt)
          
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                oneSum = row[i].get(1, 0) + col[j].get(1, 0)
                zeroSum = row[i].get(0, 0) + col[j].get(0, 0)
                diff[i][j] = oneSum - zeroSum
            
        return diff

