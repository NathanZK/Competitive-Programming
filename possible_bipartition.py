class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        group = [-1 for _ in range(n)]

        def dfs(index):
            if group[index-1] == -1:
                group[index-1] = 0

            for neighbor in graph[index]:
                if group[neighbor-1] == -1:
                    group[neighbor-1] = 1 - group[index-1]
                    if not dfs(neighbor):
                        return False

                elif group[neighbor-1] == group[index-1]:
                    return False

            return True

        for src, des in dislikes:
            graph[src].append(des)
            graph[des].append(src)

        for i in range(1, n + 1):
            if group[i-1] == -1:
                if not dfs(i):
                    return False

        return True
                    

        

        