class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        currDir = 0
        currLoc = [0, 0]

        for ints in instructions:
            if ints == "G":
                if currDir == 0:
                    currLoc[0] += 1
                elif currDir == 1:
                    currLoc[1] += 1
                elif currDir == 2:
                    currLoc[0] -= 1
                else:
                    currLoc[1] -= 1
            
            elif ints == "R":
                currDir = (currDir+1)%4
            elif ints == "L":
                currDir = (currDir-1)%4

        if currDir == 0 and (currLoc[0] != 0 or currLoc[1] != 0):
            return False


        return True