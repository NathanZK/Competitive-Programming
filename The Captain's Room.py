# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
rooms = list(map(int, input().split()))
count = {}
for r in rooms:
    count[r] = count.get(r, 0) + 1
    
for i in count:
    if count[i] == 1:
        print(i)
