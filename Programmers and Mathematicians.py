t = int(input())

def search(a, b):
   min_ = min(a, b)
   maxTeams = (a+b)//4 
   left, right = 0, maxTeams
   
   while left <= right:
      mid = (left+right)//2
      if mid > min_:
         right = mid - 1
      elif mid < min_:
         left = mid + 1
      else:
         return mid
         
   return maxTeams

for _ in range(t):
   a, b = map(int, input().split())
   
   print(search(a,b))
   
   
   
