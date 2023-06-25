from collections import defaultdict, deque

def parallelCourses(n, prerequisites):
    # Write your code here.
    graph = defaultdict(list)
    incoming = {i:0 for i in range(1,n+1)}
    queue = deque()
    numSemesters = 0
    visited = set()

    for A, B in prerequisites:
        graph[A].append(B)
        incoming[B] += 1

    for key, val in incoming.items():
        if val == 0:
            queue.append(key)

    while queue:
        size = len(queue)

        for i in range(size):
            course = queue.popleft()
            visited.add(course)

            for neighbor in graph[course]:
                incoming[neighbor] -= 1

                if incoming[neighbor] == 0:
                    queue.append(neighbor)

        numSemesters += 1

    if len(visited) == n:
        return numSemesters

    return -1
