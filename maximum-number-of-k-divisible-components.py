class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        visited = set()

        for src, des in edges:
            graph[src].append(des)
            graph[des].append(src)

        def dfs(node):
            visited.add(node)

            currSum = values[node]
            currCount = 0
            for child in graph[node]:
                if child not in visited:
                    childSum, childCount = dfs(child)
                    currSum += childSum
                    currCount += childCount

            if currSum % k == 0:
                currCount += 1

            return [currSum, currCount]

        totalSum, count = dfs(0)
        return count