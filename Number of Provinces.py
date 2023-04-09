class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        provinces = 0
        visited = set()

        for row in range(len(isConnected)):
            for col in range(len(isConnected[row])):
                if isConnected[row][col] == 1:
                    graph[row+1].append(col+1)

        for i in range(1, len(isConnected)+1):
            if i not in visited:
                provinces += 1
                self.dfs(i, visited, graph)

        return provinces

    def dfs(self, node, visited, graph):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, graph)

