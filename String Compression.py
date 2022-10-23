class Solution:
    def compress(self, chars: List[str]) -> int:
        left, next = 0, 1
        while next < len(chars):
            count = 1
            while next < len(chars) and chars[left] == chars[next]:
                count += 1
                next += 1
            if count != 1: 
                chars[left + 1: next] = str(count)
                left += len(str(count)) + 1
                next = left + 1
            else:
                left += 1
                next = left + 1
