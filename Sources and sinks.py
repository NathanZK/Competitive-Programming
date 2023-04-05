n = int(input())
adjMat = []

for _ in range(n):
    row = list(map(int, input().split()))
    adjMat.append(row)

def sourceSink(adjMat):
    sources = []
    sinks = []

    for row in range(len(adjMat)):
        num1 = 0
        for col in range(len(adjMat[row])):
            if adjMat[row][col] == 1:
                num1 = 1
                break

        if num1 == 0:
            sinks.append(row+1)

    for col in range(len(adjMat[0])):
        num1 = 0
        for row in range(len(adjMat)):
            if adjMat[row][col] == 1:
                num1 = 1
                break

        if num1 == 0:
            sources.append(col+1)

    return sources, sinks

sources, sinks = sourceSink(adjMat)
print(len(sources), *sources)
print(len(sinks), *sinks)
