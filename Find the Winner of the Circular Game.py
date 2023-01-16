class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        numList = [i for i in range(1, n + 1)]
        i = 0
        numZeros = 0
        while len(numList) - numZeros > 1:
            count = 1
            while count < k:
                while numList[i%n] == 0:
                    i += 1
                count += 1
                i += 1
            
            while numList[i%n] == 0:
                i += 1
            numList[i%n] = 0
            numZeros += 1
            i += 1

        for num in numList:
            if num != 0:
                return num


