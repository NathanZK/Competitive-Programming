t = int(input())
 
for _ in range(t):
     n = int(input())
     nums = list(map(int, input().split()))
     
     possible = "YES"
     nums.sort()
     for i in range(len(nums)-1):
          if nums[i+1] - nums[i] > 1:
               possible = "NO"
               break
     
     if len(nums) == 1:
          possible = "YES"
          
     print(possible)
