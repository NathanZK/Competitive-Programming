from math import floor, log2
 
t = int(input())
 
for _ in range(t):
   num = int(input())
   firstZero = floor(log2(num))+1
   
   ones = []
   zeroFound = False
   count = 0
   
   while num > 0:
      if num&1:
         ones.append(count)
         
      if not num&1 and not zeroFound:
         zeroFound = True
         firstZero = count
         
      num >>= 1
      count += 1
      
      if zeroFound and len(ones) > 1:
         break
      
   y = 2**(ones[0])
   if len(ones) == 1:
      y += 2**firstZero
      
   print(y)
