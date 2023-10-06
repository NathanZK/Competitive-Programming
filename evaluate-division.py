class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        visited = set()

        for i in range(len(equations)):
            src, des = equations[i]
            weight = values[i]
            graph[src].append([des, weight])
            graph[des].append([src, 1/weight])

        # print(graph)

        def dfs(node, des, currCost, visited):
            currVal = -1
            if node == des:
                return currCost

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    cost = dfs(neighbor, des, currCost*weight, visited)
                    if cost != -1:
                        currVal = cost

            return currVal

        queryAnswers = []
        for src, des in queries:
            if src not in graph or des not in graph:
                queryAnswers.append(-1)
            else:
                queryAns = dfs(src, des, 1, set())
                queryAnswers.append(queryAns)

        return queryAnswers