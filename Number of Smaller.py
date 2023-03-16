n, m = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
 
smaller = []
left = 0
for num in list2:
   while left < n and list1[left] < num:
      left += 1
      
   smaller.append(left)
   
print(*smaller)
