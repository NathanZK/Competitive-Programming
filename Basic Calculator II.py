class Solution:
    def calculate(self, s: str) -> int:
        s = self.helper(s)
        stack = []
        for i in s:
            if stack and stack[-1] == "*":
                stack.pop()
                stack.append(int(i) * int(stack.pop()))
            elif stack and stack[-1] == "/":
                stack.pop()
                stack.append(int(stack.pop()) // int(i))
            else:
                stack.append(i)
                
        s = stack
        stack = []
        for i in s:
            if stack and stack[-1] == "+":
                stack.pop()
                stack.append(int(i) + int(stack.pop()))
            elif stack and stack[-1] == "-":
                stack.pop()
                stack.append(int(stack.pop()) - int(i))
            else:
                stack.append(i)
                
        return int(stack[0])
  

    def helper(self, s):
        stack = []
        ops = "+-*/"
        st = ""
        for n, i in enumerate(s):
            if i in ops and st != "":
                stack.append(st)
                stack.append(i)
                st = ""
            elif n == len(s) - 1:
                st += i
                stack.append(st)
            else:
                st += i
                
        return stack
            
