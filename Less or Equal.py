n, k = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

if k == 0 and nums[0] > 1:
     print(1)
elif k < n and nums[k] <= nums[k-1]:
     print(-1)
else:
     print(nums[k-1])
