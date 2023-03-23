n, k = map(int, input().split())
players = list(map(int, input().split()))

def mergeSort(start, end, arr, diff):
   if start == end:
      return [start]
      
   mid = (start+end)//2
   leftArr = mergeSort(start, mid, arr, diff)
   rightArr = mergeSort(mid+1, end, arr, diff)
   
   return merge(leftArr, rightArr, arr, diff)
   
def merge(arr1, arr2, nums, diff):
   p1, p2 = 0, 0
   minLeft, minRight = nums[arr1[0]], nums[arr2[0]]
   
   while p1 < len(arr1) and nums[arr1[p1]] < minRight - diff:
      p1 += 1
      
   while p2 < len(arr2) and nums[arr2[p2]] < minLeft - diff:
      p2 += 1
   
   merged = []
   
   while p1 < len(arr1) and p2 < len(arr2):
      if nums[arr1[p1]] < nums[arr2[p2]]:
         merged.append(arr1[p1])
         p1 += 1
      
      else:
         merged.append(arr2[p2])
         p2 += 1
         
   merged.extend(arr1[p1:])
   merged.extend(arr2[p2:])
   
   return merged
   
couldWin = mergeSort(0, len(players)-1, players, k)
couldWin = sorted(map(lambda x: x+1, couldWin))
print(*couldWin)
      
      
      
      
      
      
      
