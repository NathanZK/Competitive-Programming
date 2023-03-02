class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        maxPath = [0,0]

        for col in range(len(grid[0])-2, 0, -1):
            grid[0][col] += grid[0][col+1]

        for col in range(1, len(grid[0])):
            grid[1][col] += grid[1][col-1]

        for col in range(1, len(grid[0])):
            if grid[0][col] > grid[1][col-1]:
                maxPath = [0, col]
            else:
                break
        
        if len(grid[0]) == 1:
            return 0
        elif maxPath[1] == len(grid[0]) - 1:
            return grid[1][maxPath[1] - 1]
        elif maxPath[1] == 0:
            return grid[0][1]
        else:
            return max(grid[0][maxPath[1]+1], grid[1][maxPath[1]-1])
