n = int(input())
 
nums = list(map(int, input().split()))
odd, even = False, False
for num in nums:
     if even and odd:
          break
     elif num % 2 == 1:
          odd = True
     else:
          even = True
          
if even and odd:
     nums.sort()
print(*nums)
