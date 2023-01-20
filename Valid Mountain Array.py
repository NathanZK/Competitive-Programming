class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
            
        inc, dec = False, False
        for i in range(1,len(arr)):
            if arr[i] > arr[i - 1]:
                if dec == True:
                    return False
                inc = True
            elif arr[i] < arr[i - 1]:
                if inc == False:
                    return False
                dec = True
            else:
                return False

        return inc and dec
