# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

for t in range(T):
    n = int(input())
    nVals = list(map(int, input().split()))

    l, r = 0, n - 1
    maxVal = float('inf')
    
    while l < r:
        if max(nVals[l], nVals[r]) <= maxVal:
            maxVal = max(nVals[l], nVals[r])
            if nVals[l] < nVals[r]:
                r -= 1
            else:
                l += 1
        else:
            print("No")
            break
    if (l == r):     
        print("Yes")
