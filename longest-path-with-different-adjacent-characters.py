class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)

        for i in range(1, len(parent)):
            graph[parent[i]].append(i)

        self.longestPath = 1
        self.dfs(0, graph, s)

        return self.longestPath

    def dfs(self, node, graph, s):
        longest, secLongest = 0, 0

        for neighbor in graph[node]:
            pathLength = self.dfs(neighbor, graph, s)

            if s[neighbor] != s[node]:
                if pathLength > longest:
                    secLongest = longest
                    longest = pathLength
                else:
                    secLongest = max(secLongest, pathLength)

        self.longestPath = max(self.longestPath, longest + secLongest + 1)
        return longest + 1