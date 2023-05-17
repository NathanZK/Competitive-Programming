class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incoming = Counter()
        queue = deque()
        order = []
        ends = []

        for src, des in adjacentPairs:
            graph[src].append(des)
            graph[des].append(src)
            incoming[src] += 1
            incoming[des] += 1

        for val in incoming.keys():
            if incoming[val] == 1:
                ends.append(val)

        queue.append(ends[0])
        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbor in graph[node]:
                incoming[neighbor] -= 1

                if incoming[neighbor] == 1:
                    queue.append(neighbor)


        order.append(ends[1])
        return order