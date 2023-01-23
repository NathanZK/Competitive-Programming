class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        sort = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                sort = False    
        if sort:
            return []
        
        kFlips = []
        end = len(arr) - 1
        while end > 0:
            max_ = arr.index(max(arr[:end+1]))
            self.reverse(arr, 0, max_)
            self.reverse(arr, 0, end)
            kFlips.append(max_+1)
            kFlips.append(end+1)
            end -= 1

        return kFlips
      
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        
        
