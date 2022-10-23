class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        add = 0
        sub = 0
        while sub < len(popped) and add < len(pushed):
            if pushed[add] == popped[sub]:
                pushed.pop(add)
                sub += 1
                if add != 0: add -= 1
            else:
                add += 1
        return len(pushed) == 0
