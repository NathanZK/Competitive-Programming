class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        maxBombs = 0

        def bombRegion(node, bomb):
            radius = (bomb[1]-node[1])**2 + (bomb[0]-node[0])**2
            return radius <= node[2]**2

        def dfs(index, bombed):
            bombed[index] = True

            detonated = 0
            for i in range(len(bombs)):
                if not bombed[i] and bombRegion(bombs[index], bombs[i]):
                    detonated += 1 + dfs(i, bombed)
                
            return detonated

        for i in range(len(bombs)):
            maxBombs = max(maxBombs, 1 + dfs(i, [False] * len(bombs)))

        return maxBombs