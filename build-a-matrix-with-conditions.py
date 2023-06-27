class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rowLoc = self.topSort(k, rowConditions)
        colLoc = self.topSort(k, colConditions)

        if rowLoc == 0 or colLoc == 0:
            return []

        mat = [[0 for _ in range(k)] for _ in range(k)]
        for i in range(1, k+1):
            mat[rowLoc[i]][colLoc[i]] = i

        return mat

    def topSort(self, k, conditions):
        graph = defaultdict(list)
        incoming = {i:0 for i in range(1, k+1)}
        queue = deque()
        count = 0
        location = {}

        for before, after in conditions:
            graph[before].append(after)
            incoming[after] += 1

        for i in range(1, k+1):
            if incoming[i] == 0:
                queue.append(i)

        while queue:
            num = queue.popleft()
            location[num] = count
            count += 1

            for neighbor in graph[num]:
                incoming[neighbor] -= 1

                if incoming[neighbor] == 0:
                    queue.append(neighbor)

        if count == k:
            return location
        
        return 0