n = int(input())

for _ in range(n):
     res = "="
     size1, size2 = input().split()
     if (size1[-1] == "L" or size1[-1] == "M") and size2[-1] == "S":
          res = ">"
     elif size1[-1] == "L" and size2[-1] == "M":
          res = ">"
     elif size1[-1] == size2[-1]:
          if size1[-1] == "S":
               if len(size1) > len(size2):
                    res = "<"
               elif len(size1) < len(size2):
                    res = ">"
               else:
                    res = "="
          elif size1[-1] == "M":
               res = "="
          else:
               if len(size1) < len(size2):
                    res = "<"
               elif len(size1) > len(size2):
                    res = ">"
               else:
                    res = "="
               
     else:
          res = "<"
     
     print(res)  
     
