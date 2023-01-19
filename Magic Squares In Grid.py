class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if n < 3 or m < 3:
            return 0

        magic = True
        magicCount = 0
        for i in range(n-2):
            for j in range(m-2):
                nums = set(grid[i][j:j+3])
                val = sum(grid[i][j:j+3])
                dig1 = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] 
                dig2 = grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2]
                if dig1 != val or dig2 != val:
                    magic = False
                for r in range(3):
                    row = grid[i+r][j:j+3]
                    Sum = sum(row)
                    if Sum != val:
                        magic = False
                        break
                    nums.update(row)
                for c in range(3):
                    col = [grid[i][j+c], grid[i+1][j+c],grid[i+2][j+c]]
                    Sum = sum(col)
                    if Sum != val:
                        magic = False
                        break
                    nums.update(col)
                
                min_ = min(list(nums))
                max_ = max(list(nums))
                if magic and len(nums) == 9 and min_ == 1 and max_ == 9:
                    magicCount += 1
                magic = True
                
        return magicCount
