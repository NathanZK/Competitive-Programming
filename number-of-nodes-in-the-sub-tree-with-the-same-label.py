class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        sameLabel = [1] * n
        visited = set()

        for src, des in edges:
            graph[src].append(des)
            graph[des].append(src)

        def dfs(node):
            currDict = Counter()
            visited.add(node)

            if len(graph[node]) == 0:
                currDict[labels[node]] += 1
                return currDict

            for child in graph[node]:
                if child not in visited:
                    currDict.update(dfs(child))

            currDict[labels[node]] += 1
            sameLabel[node] = currDict[labels[node]]
            return currDict

        dfs(0)
        return sameLabel