class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)
        incoming = {i: 0 for i in range(n)}
        queue = deque()

        for src, des in edges:
            graph[src].append(des)
            graph[des].append(src)
            incoming[src] += 1
            incoming[des] += 1

        for i in range(n):
            if incoming[i] == 1:
                queue.append(i)

        while n > 2:
            size = len(queue)
            n -= size

            for i in range(size):
                node = queue.popleft()

                for neighbor in graph[node]:
                    incoming[neighbor] -= 1

                    if incoming[neighbor] == 1:
                        queue.append(neighbor)

        return list(queue)