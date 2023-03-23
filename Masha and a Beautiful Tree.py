t = int(input())

ops = 0
def merge(arr1, arr2):
   global ops
   
   if arr1[0] <= arr2[0]:
      arr1.extend(arr2)
      return arr1
   else:
      ops += 1
      arr2.extend(arr1)
      return arr2


def mergeSort(start, end, arr):
   global ops
   
   if start == end:
      return [nums[start]]
      
   mid = (start+end)//2
   leftArr = mergeSort(start, mid, arr)
   rightArr = mergeSort(mid+1, end, arr)
   
   return merge(leftArr, rightArr)
   

for _ in range(t):
   ops = 0
   
   m = int(input())
   nums = list(map(int, input().split()))
   arr =  mergeSort(0, len(nums)-1, nums)
   
   if arr == sorted(arr):
      print(ops)
      
   else:
      print(-1)

   
   

      
      
   
      
