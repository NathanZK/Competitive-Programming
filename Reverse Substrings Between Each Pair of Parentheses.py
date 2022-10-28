class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i == ")":
                rev = []
                while stack[-1] != "(":
                    rev.append(stack.pop())
                stack.pop()
                stack.extend(rev)
            else:
                stack.append(i)
        return "".join(stack)
