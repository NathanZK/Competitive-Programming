class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hashmap = {}
        count = 0
        for g in grid:
            row = ""
            for i in g:
                row += '#' + str(i)
            hashmap[row] = hashmap.get(row, 0) + 1

        for i in range(len(grid[0])):
            col = ""
            for j in range(len(grid)):
                col += '#' + str(grid[j][i])

            if col in hashmap:
                count += hashmap[col]

        return count