class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        N = len(num)

        for left in range(1, N):
            for right in range(left+1, N):
                if num[left] == "0" and right > left + 1:
                    break

                first, second = int(num[:left]),int(num[left:right])
                third = str(first + second)

                start, end = right, right + len(third)
                if third != num[start:end]:
                    continue

                while third == num[start: end]:
                    if end == N:
                        return True

                    first, second = second, int(third)
                    third = str(first + second)

                    start, end = end, end + len(third)

            if num[0] == "0":
                break

        return False
