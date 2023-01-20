#User function Template for python3

class Solution: 
    def selectionSort(self, arr,n):
        for i in range(n):
            minInd = i
            for j in range(i, n):
                if arr[j] < arr[minInd]:
                    minInd = j
                    
            arr[minInd], arr[i] = arr[i], arr[minInd]
            
