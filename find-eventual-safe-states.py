class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adjGraph = defaultdict(list)
        incoming = Counter()
        safeNodes = []
        queue = deque()

        for i in range(len(graph)):
            for neighbor in graph[i]:
                adjGraph[neighbor].append(i)

            incoming[i] = len(graph[i])

        for node in range(len(graph)):
            if incoming[node] == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()
            safeNodes.append(node)

            for neighbor in adjGraph[node]:
                incoming[neighbor] -= 1

                if incoming[neighbor] == 0:
                    queue.append(neighbor)

        return sorted(safeNodes)