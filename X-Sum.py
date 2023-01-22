test_case = int(input())
 
for _ in range(test_case):
     n, m = map(int, input().split())
     board = []
 
     for _ in range(n):
          row = [int(num) for num in input().split()]
          board.append(row)
     
     dig1, dig2 = {}, {}
     for row in range(n):
          for col in range(m):
               dig1[row-col] = dig1.get(row-col,0) + board[row][col]
               dig2[row+col] = dig2.get(row+col,0) + board[row][col]
     
     max_ = 0
     for row in range(n):
          for col in range(m):
               value = dig1[row-col]+dig2[row+col] - board[row][col]
               max_ = max(max_, value)
               
     print(max_)
