n, m = map(int, input().split())
 
grid = []
for _ in range(n):
     grid.append(input())
     
horCount, verCount = {}, {}
for row in range(len(grid)):
     for col in range(len(grid[0])):
          char = str(row) + grid[row][col]
          horCount[char] = horCount.get(char,0) + 1
          
for col in range(len(grid[0])):
     for row in range(len(grid)):
          char = str(col) + grid[row][col]
          verCount[char] = verCount.get(char,0) + 1
          
encrypted = []
for row in range(len(grid)):
     for col in range(len(grid[0])):
          char1 = str(row) + grid[row][col]
          char2 = str(col) + grid[row][col]
          rCount = horCount[char1]
          cCount = verCount[char2]
          if rCount == 1 and cCount == 1:
               encrypted.append(grid[row][col])
               
print("".join(encrypted))
