class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if stack and char == stack[-1][0]:
                popped, count = stack.pop()
                if 1 + count != k:
                    stack.append([char, 1 + count])
            else:
                stack.append([char, 1])

        finalString = []
        for char, count in stack:
            curr = count * char
            finalString.append(curr)

        return "".join(finalString)