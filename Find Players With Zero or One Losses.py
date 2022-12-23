class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        hashmap = {}
        #Initializing all values to zero
        for match in matches:
            hashmap[match[0]] = 0
            hashmap[match[1]] = 0

        for match in matches:
            hashmap[match[1]] = hashmap.get(match[1], 0) - 1

        noLoss, oneLoss = [], []
        for player, lost in hashmap.items():
            if lost == 0:
                noLoss.append(player)
            elif lost == -1:
                oneLoss.append(player)

        noLoss.sort()
        oneLoss.sort()
        return [noLoss, oneLoss]

