class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []

        def dfs(node, path):
            if path[-1] == len(graph) - 1:
                paths.append(path[:])
                return
            
            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()

        dfs(0, [0])
        return paths