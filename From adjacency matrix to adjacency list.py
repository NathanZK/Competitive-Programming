n = int(input())

adjMat = []
for _ in range(n):
    row = list(map(int, input().split()))
    adjMat.append(row)

graph = [[] for i in range(n)]

for row in range(len(adjMat)):
    for col in range(len(adjMat[row])):
        if adjMat[row][col]:
            graph[row].append(col+1)

for vertix in graph:
    print(len(vertix), *vertix)
