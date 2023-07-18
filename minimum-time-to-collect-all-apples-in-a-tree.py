class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        visited = set()

        for src, des in edges:
            graph[src].append(des)
            graph[des].append(src)

        def dfs(node):
            visited.add(node)
            if len(graph[node]) == 1 and node != 0:
                return 0 if hasApple[node] else -1

            collectTime = 0
            for child in graph[node]:
                if child not in visited:
                    time = dfs(child)
                    if time != -1:
                        collectTime += (time+2)

            if collectTime == 0:
                return 0 if hasApple[node] else -1

            return collectTime

        minTime = dfs(0)
        return minTime if minTime != -1 else 0