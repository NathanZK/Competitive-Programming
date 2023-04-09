"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph= {}

        for i in range(len(employees)):
            graph[employees[i].id] = [employees[i].importance, employees[i].subordinates]

        def dfs(id, visited):
            if id in visited:
                return 0

            visited.add(id)
            total = graph[id][0]
            for subordinate in graph[id][1]:
                total += dfs(subordinate, visited)
                
            return total

        return dfs(id, set())


