class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        runningSum = [0] * (len(s)+1)
        for ind in shifts:
            inc = 1 if ind[2] == 1 else -1
            runningSum[ind[0]] += inc
            runningSum[ind[1]+1] -= inc

        for i in range(1, len(runningSum)):
            runningSum[i] += runningSum[i-1]
        
        string = list(s)
        for c in range(len(s)):
            asci = ord(string[c]) + runningSum[c] % 26
            if asci > 122:
                asci -= 26
            string[c] = chr(asci)

        return "".join(string)
