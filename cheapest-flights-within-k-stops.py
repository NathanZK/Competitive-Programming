class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        n = len(flights)
        graph = defaultdict(list)
        minHeap = [[0, src, -1]]
        visited = set()

        for s, d, w in flights:
            graph[s].append([d, w])

        while minHeap:
            dist, node, stop = heappop(minHeap)
            if (node, stop) in visited:
                continue
            
            visited.add((node, stop))
            if node == dst:
                return dist

            if stop == k and node != dst:
                continue

            for neighbor, weight in graph[node]:
                currDist = dist + weight

                heappush(minHeap,[currDist, neighbor, stop+1])

        return -1