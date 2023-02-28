class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
            
        arr = self.getRow(rowIndex-1)
        currArr = [1] * (rowIndex+1)

        for i in range(1, rowIndex):
            currArr[i] = arr[i-1] + arr[i]

        return currArr
