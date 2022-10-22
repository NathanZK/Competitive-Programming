class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key = lambda x: x[1])
        numPass = trips[0][0]
        if numPass > capacity:
            return False
        trP = trips.copy()
        for n in range(1, len(trips)):
            numPass += trips[n][0]
            start = trips[n][1]
            i = 0
            m = n
            while i < m:
                try:
                    if start >= trP[i][2]:
                        numPass -= trP[i][0]
                        trP.pop(i)
                        m -= 1
                        continue
                except:
                    pass
                i += 1
            if numPass > capacity:
                return False
        return True
