class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row, col = len(dungeon)-1, len(dungeon[0])-1
        dungeon[row][col] = min(0, dungeon[row][col])

        for r in range(row, -1, -1):
            for c in range(col, -1, -1):
                if (r, c) == (row, col):
                    continue

                if r == row:
                    dungeon[r][c] = min(dungeon[r][c]+dungeon[r][c+1], 0)
                elif c == col:
                    dungeon[r][c] = min(dungeon[r][c]+dungeon[r+1][c], 0)
                else:
                    dungeon[r][c] += max(dungeon[r+1][c], dungeon[r][c+1])
                    dungeon[r][c] = min(dungeon[r][c], 0)

        return abs(dungeon[0][0])+1