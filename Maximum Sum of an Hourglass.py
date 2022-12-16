class Solution(object):
    def maxSum(self, grid):
        maxSum = 0
        j = 0
        while j + 2 < len(grid):
            i = 0
            while i + 2 < len(grid[0]):
                sum = grid[j][i] + grid[j][i + 1] + grid[j][i + 2]
                sum += grid[j + 1][i + 1]
                sum += grid[j + 2][i] + grid[j + 2][i + 1] + grid[j + 2][i + 2]
                maxSum = max(maxSum, sum)
                i += 1
            j += 1
        return maxSum
        
