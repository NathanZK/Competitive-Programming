class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        sortedArr = sorted(arr)
        if sortedArr == arr:
            return arr

        for i in range(len(arr)-1,-1,-1):
            largestInd = len(arr)
        
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    if largestInd == len(arr) or arr[j] > arr[largestInd]:
                        largestInd = j

            if largestInd != len(arr):
                arr[largestInd], arr[i] = arr[i], arr[largestInd]
                return arr