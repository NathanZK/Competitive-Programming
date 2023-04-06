class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for src, des in edges:
            graph[src].append(des)

        for key, val in graph.items():
            for v in val:
                if v != -1 and v in graph:
                    graph[v].append(-1)

        smallestVertices = []
        for key, val in graph.items():
            if val[-1] != -1:
                smallestVertices.append(key)

        return smallestVertices
