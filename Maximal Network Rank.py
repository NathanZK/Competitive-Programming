class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = [set() for _ in range(n)]
        maxNetwork = 0

        for src, des in roads:
            graph[src].add(des)
            graph[des].add(src)

        for i in range(len(graph)):
            for j in range(i+1, len(graph)):
                if i in graph[j]:
                    maxNetwork = max(maxNetwork, len(graph[i]) + len(graph[j]) - 1)
                else:
                    maxNetwork = max(maxNetwork, len(graph[i]) + len(graph[j]))

        return maxNetwork
