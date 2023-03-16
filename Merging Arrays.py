n, m = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
merged = []
 
p1, p2 = 0, 0
while p1 < n and p2 < m:
   if list1[p1]<list2[p2]:
      merged.append(list1[p1])
      p1 += 1
      
   else:
      merged.append(list2[p2])
      p2 += 1
      
merged.extend(list1[p1:])
merged.extend(list2[p2:])
 
print(*merged)
