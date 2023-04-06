n = int(input())
roads = 0

for _ in range(n):
    row = list(map(int, input().split()))
    for r in row:
        if r == 1:
            roads += 1

print(roads//2)
