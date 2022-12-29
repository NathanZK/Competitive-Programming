import collections

n = int(input())
for i in range(n):
     money = 0
     numP, cost = map(int, input().split())
     hashPlanet = collections.Counter(list(map(int, input().split())))
     
     for val in hashPlanet.values():
          if val < cost:
               money += val
          else:
               money += cost
     
     print(money)
