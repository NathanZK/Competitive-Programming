class Solution:
    def maxLength(self, arr: List[str]) -> int:
        maxL = 0

        def dfs(index, sub):
            nonlocal maxL

            seq = "".join(sub)
            if len(seq) != len(set(seq)):
                return

            if len(seq) == len(set(seq)):
                maxL = max(maxL, len(seq))

            if index >= len(arr):
                return
            
            sub.append(arr[index])
            dfs(index+1, sub)
            sub.pop()

            dfs(index+1, sub)

        dfs(0, [])
        return maxL
