# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
nVal = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happiness = 0
for num in nVal:
    if num in A:
        happiness += 1
    if num in B:
        happiness -= 1
        
print(happiness)
