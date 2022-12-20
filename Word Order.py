# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(input())
distinctNums = {}
for n in range(num):
    new = input()
    if new in distinctNums:
        distinctNums[new] += 1
    else:
        distinctNums[new] = 1
        
print(len(distinctNums))
for i in distinctNums.values():
    print(i, end = " ")
