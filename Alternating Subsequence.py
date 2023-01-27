t = int(input())

for _ in range(t):
     n = int(input())
     nums = list(map(int, input().split()))
     
     left = 0
     maxSum = 0
     for read in range(len(nums)):
          if nums[read] * nums[left] < 0:
               maxSum += nums[left]
               left = read
               
          else:
               if nums[read] > nums[left]:
                    left = read
                    
     maxSum += nums[left]
     print(maxSum)
