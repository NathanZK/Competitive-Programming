class Solution:
    def calculate(self, s: str) -> int:
        nums = self.separateNums(s.strip())
        stack = []

        for n in nums:
            if n.isdigit():
                if stack and (stack[-1] == "*" or stack[-1] == "/"):
                    op = stack.pop()
                    num = stack.pop()

                    if op == "*":
                        stack.append(int(n)*num)
                    else:
                        stack.append(num//int(n))
                else:
                    stack.append(int(n))
            else:
                stack.append(n)

        nums = stack
        stack = []
        for n in nums:
            if str(n).isdigit():
                if stack and (stack[-1] == "+" or stack[-1] == "-"):
                    op = stack.pop()
                    num = stack.pop()

                    if op == "+":
                        stack.append(n+num)
                    else:
                        stack.append(num-n)
                else:
                    stack.append(n)
            else:
                stack.append(n) 

        return stack[0]
 

    def separateNums(self, s):
        stack = []
        i = 0

        while i < len(s):
            curr = []
            while i < len(s) and s[i].isdigit():
                curr.append(s[i])
                i += 1

            if curr:
                stack.append("".join(curr))

            if i < len(s) and s[i] != " ":
                stack.append(s[i])

            i+= 1

        return stack