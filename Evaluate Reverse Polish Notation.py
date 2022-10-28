class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = "+-*/"
        for n in tokens:
            if n in operations:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if n == "+":
                    res = num1 + num2
                if n == "-":
                    res = num1 - num2
                if n == "*":
                    res = num1 * num2
                if n == "/":
                    res = int(num1 / num2)
                stack.append(res)
            else:
                stack.append(n)
        return stack[0]
