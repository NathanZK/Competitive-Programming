from typing import List


from typing import List
from collections import defaultdict, deque


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        graph = defaultdict(list)
        incoming = {i: 0 for i in range(1, n+1)}
        queue = deque()
        time = [0] * (n+1)
        
        for src, des in edges:
            graph[src].append(des)
            incoming[des] += 1
            
        for i in range(1, n+1):
            if incoming[i] == 0:
                queue.append(i)
                time[i] = 1
                
        while queue:
            job = queue.popleft()
            
            for neighbor in graph[job]:
                incoming[neighbor] -= 1
                
                if incoming[neighbor] == 0:
                    queue.append(neighbor)
                    time[neighbor] = time[job] + 1
        
        ans = [str(n) for n in time[1:]]
        return " ".join(ans)
        
                



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        print(res)
        

# } Driver Code Ends
