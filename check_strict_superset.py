# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
N = int(input())

res = True
for _ in range(N):
    B = set(map(int, input().split()))
    if len(A - B) == 0 or len(B - A) > 0:
        res = False
        
print(res)
