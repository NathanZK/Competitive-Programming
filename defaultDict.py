# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split())
A = []
B = []

for _ in range(n):
    A.append(input())   
for _ in range(m):
    B.append(input())
    
d = defaultdict(list)
for ind, char in enumerate(A):
    d[char].append(str(ind + 1))
    
for char in B:
    if d[char]:
        print(" ".join(d[char]))
    else:
        print("-1")
