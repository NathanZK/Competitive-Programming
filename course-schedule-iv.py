class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        queue = deque()
        preList = [set() for _ in range(numCourses)]
        incoming = [0] * numCourses

        for pre, course in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1

        for i in range(numCourses):
            if incoming[i] == 0:
                queue.append(i)

        while queue:
            course = queue.popleft()

            for neighbor in graph[course]:
                preList[neighbor].add(course)
                preList[neighbor].update(preList[course])

                incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    queue.append(neighbor)

        answer = []
        for cor1, cor2 in queries:
            answer.append(cor1 in preList[cor2])

        return answer