class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [0 for _ in range(n)]
        for src, des in edges:
            graph[des] = 1
        
        smallest = []
        for i in range(len(graph)):
            if graph[i] == 0:
                smallest.append(i)

        return smallest
