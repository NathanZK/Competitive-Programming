class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        translation = Counter()
        length = len(img1)

        for row in range(length):
            for col in range(length):
                if img1[row][col] == 0:
                    continue

                for i in range(length):
                    diffRow = i - row

                    for j in range(length):
                        diffCol = j - col
                        if img2[row+diffRow][col+diffCol]:
                            translation[(diffRow, diffCol)] +=1
 
        values = translation.values()
        if not values:
            return 0

        return max(values)