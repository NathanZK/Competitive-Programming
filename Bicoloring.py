from collections import defaultdict, deque

while True:
    n = int(input())
    if n == 0:
        break
    edges = int(input())

    graph = defaultdict(list)
    for _ in range(edges):
        src, des = map(int, input().split())
        graph[src].append(des)
        graph[des].append(src)

    color = {i:-1 for i in range(1, n+1)}

    queue = deque([1])
    color[1] = 0
    colorable = True

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if color[neighbor] == -1:
                color[neighbor] = 1 - color[node]
                queue.append(neighbor)
            elif color[neighbor] == color[node]:
                colorable = False
                break

    if colorable:
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")
