class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        currGas = 0
        station = 0
        for i in range(len(gas)):
            currGas += gas[i] - cost[i]
            if currGas < 0:
                currGas = 0
                station = i+1

        return station