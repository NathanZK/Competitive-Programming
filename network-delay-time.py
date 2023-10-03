class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for start, end, weight in times:
            graph[start].append([end, weight])

        shortest = {node: float('inf') for node in range(1, n+1)}
        shortest[k] = 0
        visited = set()

        minHeap = [(0, k)]
        while minHeap:
            nodeDist, currNode = heappop(minHeap)
            if currNode in visited:
                continue
            visited.add(currNode)

            for neighbor, neighborWeight in graph[currNode]:
                currDist = nodeDist + neighborWeight
                if currDist < shortest[neighbor]:
                    shortest[neighbor] = currDist
                    heappush(minHeap, [currDist, neighbor])

        if len(visited) == n:
            return max(shortest.values())

        return -1