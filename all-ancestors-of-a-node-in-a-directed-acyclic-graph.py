class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        ancestors = [set() for _ in range(n)]
        incoming = Counter()
        queue = deque()

        for src, des in edges:
            graph[src].append(des)
            incoming[des] += 1

        for node in range(n):
            if incoming[node] == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()

            for descendant in graph[node]:
                incoming[descendant] -= 1
                ancestors[descendant].add(node)
                ancestors[descendant].update(ancestors[node])

                if incoming[descendant] == 0:
                    queue.append(descendant)

        for i in range(len(ancestors)):
            ancestors[i] = sorted(ancestors[i])
            
        return ancestors