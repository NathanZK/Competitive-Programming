from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
        visited = set()
        def dfs(node, path, parent):
            visited.add(node)
            path.add(node)
            
            for neighbor in adj[node]:
                if neighbor in path and neighbor != parent:
                    return True
                elif neighbor not in visited:
                    if dfs(neighbor, path, node):
                        return True
            
            return False
            
        for i in range(V):
            if i not in visited:
                if dfs(i, set(), -1):
                    return 1
                    
        return 0

#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
