class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        order = []

        for i in range(len(tasks)):
            tasks[i].insert(1, i)

        tasks.sort()
        time = tasks[0][0]
        
        i = 0
        while i<len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heappush(heap, (tasks[i][2], tasks[i][1]))
                i += 1
            if not heap:
                time = tasks[i][0]
            else:
                shortest = heappop(heap)
                order.append(shortest[1])
                time += shortest[0]

        while heap:
            shortestTime, index = heappop(heap)
            order.append(index)

        return order