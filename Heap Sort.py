#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        bigger_child = i
        left = 2*i + 1
        right = 2*i + 2
        
        if left < n and arr[bigger_child] < arr[left]:
            bigger_child = left
            
        if right < n and arr[bigger_child] < arr[right]:
            bigger_child = right
            
        if bigger_child != i:
            arr[bigger_child], arr[i] = arr[i], arr[bigger_child]
            self.heapify(arr, n, bigger_child)
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(n//2 - 1, -1, -1):
            self.heapify(arr, n, i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        
        self.buildHeap(arr, n)
        last = n - 1
        while last > 0:
            arr[0], arr[last] = arr[last], arr[0]
            self.heapify(arr, last, 0)
            last -= 1



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends
