class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        size = len(edges)
        count = {}

        for src, des in edges:
            count[src] = count.get(src, 0) + 1
            count[des] = count.get(des, 0) + 1
            
            if count[src] == size:
                return src
            if count[des] == size:
                return des
