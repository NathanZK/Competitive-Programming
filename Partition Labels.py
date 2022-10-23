class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start = 0
        left, pos, right = 0, 0, 1
        output = []
        while left < len(s) and right < len(s):
            if s[left] == s[right]:
                pos = right
            if pos == len(s) - 1:
                output.append(pos - start + 1)
                break
            right += 1
            if right == len(s):
                if left == pos:
                    output.append(pos - start + 1)
                    start = left + 1
                    left += 1
                    pos = left
                    right = left + 1
                else:
                    left += 1
                    right = pos + 1
                if left == len(s) - 1:
                    output.append(1)
        return output
