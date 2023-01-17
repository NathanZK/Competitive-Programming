class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid) - 2
        maxLocal = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                max1 = max(grid[i][j:j+3])
                max2 = max(grid[i+1][j:j+3])
                max3 = max(grid[i+2][j:j+3])
                maxLocal[i][j] = max(max1,max2,max3)
        return maxLocal
 
