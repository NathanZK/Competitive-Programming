class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix = [0] * 1002
        for num, start, end in trips:
            prefix[start] += num
            prefix[end] -= num

        runningSum = 0
        for i in range(len(prefix)-1):
            runningSum += prefix[i]
            if runningSum > capacity:
                return False

        return True
        
