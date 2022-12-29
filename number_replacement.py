n = int(input())

for _ in range(n):
     length = int(input())
     nums = list(map(int, input().split()))
     string = input()
     res = "YES"
     
     hashmap = {}
     for i, n in enumerate(nums):
          if n not in hashmap:
               hashmap[n] = string[i]
          elif hashmap[n] != string[i]:
               res = "NO"
               break
          
     print(res)
               
     
