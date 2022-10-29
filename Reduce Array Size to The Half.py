class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        length = len(arr)
        size = 0
        count = {}
        for n in arr:
            count[n] = count.get(n, 0) + 1
        count = dict(sorted(count.items(), key = lambda x:x[1], reverse = True))
        
        for num in count.keys():
            length -= count[num]
            size += 1
            if length <= len(arr) / 2:
                return size
