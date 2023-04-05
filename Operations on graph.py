from collections import defaultdict

n = int(input())
ops = int(input())
graph = defaultdict(list)

for _ in range(ops):
    opDes = list(map(int, input().split()))
    
    if opDes[0] == 1:
        graph[opDes[1]].append(opDes[2])
        graph[opDes[2]].append(opDes[1])

    if opDes[0] == 2:
        if graph[opDes[1]]:
            print(*graph[opDes[1]])
