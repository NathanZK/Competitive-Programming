class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def bombRegion(node, bomb):
            radius = (bomb[1]-node[1])**2 + (bomb[0]-node[0])**2
            return radius <= node[2]**2

        graph = defaultdict(list)
        maxBombs = 0
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j and bombRegion(bombs[i], bombs[j]):
                    graph[i].append(j)

        def dfs(index, bombed):
            bombed.add(index)

            detonated = 0
            for neighbor in graph[index]:
                if neighbor not in bombed:
                    detonated += 1 + dfs(neighbor, bombed)

            return detonated
        
        keys = list(graph.keys())
        for key in keys:
            maxBombs = max(maxBombs, 1 + dfs(key, set()))
        
        return max(1, maxBombs)