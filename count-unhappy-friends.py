class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        hashPairs = {}
        for num1, num2 in pairs:
            hashPairs[num1] = num2
            hashPairs[num2] = num1
        
        unhappy = set()
        for i in range(n):
            if i in unhappy:
                continue

            pair1 = hashPairs[i]
            for p1 in preferences[i]:
                if p1 == pair1:
                    break

                pair2 = hashPairs[p1]
                for p2 in preferences[p1]:
                    if p2 == pair2:
                        break

                    if p2 == i:
                        unhappy.add(i)
                        unhappy.add(p1)

        return len(unhappy)