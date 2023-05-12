#User function Template for python3
from collections import defaultdict, Counter, deque

class Solution:
    def findOrder(self,alien_dict, N, K):
        graph = defaultdict(set)
        incoming = Counter()
        queue = deque()
        order = []
        keys = set()
        
        for i in range(len(alien_dict)-1):
            keys.update(alien_dict[i])
            keys.update(alien_dict[i+1])
            if alien_dict[i][0] != alien_dict[i+1][0]:
                if alien_dict[i+1][0] not in graph[alien_dict[i][0]]:
                    graph[alien_dict[i][0]].add(alien_dict[i+1][0])
                    incoming[alien_dict[i+1][0]] += 1
                
            else:
                ptr = 1
                while ptr < len(alien_dict[i]) and ptr < len(alien_dict[i+1]) and alien_dict[i][ptr] == alien_dict[i+1][ptr]:
                    ptr += 1

                if ptr < len(alien_dict[i]) and ptr < len(alien_dict[i+1]):
                    if alien_dict[i+1][ptr] not in graph[alien_dict[i][ptr]]:
                        graph[alien_dict[i][ptr]].add(alien_dict[i+1][ptr])
                        incoming[alien_dict[i+1][ptr]] += 1
        
        for k in list(keys):
            if incoming[k] == 0:
                queue.append(k)
                
        while queue:
            node = queue.popleft()
            order.append(node)
            
            for neighbor in graph[node]:
                incoming[neighbor] -= 1
                
                if incoming[neighbor] == 0:
                    queue.append(neighbor)
        
        return order
        
    # code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends
