class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(points)):
            xI, yI = points[i]
            for j in range(i+1, len(points)):
                xJ, yJ = points[j]
                dist = abs(xI-xJ)+ abs(yI-yJ)
                graph[i].append([j, dist])
                graph[j].append([i, dist])

        queue = deque([0])
        visited = set()
        minHeap = [(0,0)]
        minCost = 0

        while len(visited) < len(points):
            leastCost, node = heappop(minHeap)
            if node in visited:
                continue 
            minCost += leastCost
            visited.add(node)
            
            for neighbor, cost in graph[node]:
                if neighbor not in visited:
                    heappush(minHeap, (cost, neighbor))

        return minCost