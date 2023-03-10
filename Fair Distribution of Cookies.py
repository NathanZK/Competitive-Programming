class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.unfair = float("inf")

        def dfs(index, kids):
            if max(kids) >= self.unfair:
                return

            if index == len(cookies):
                unfairness = max(kids)
                self.unfair = min(self.unfair, unfairness)
                return

            leftCookies = len(cookies) - index
            cryingKids = 0
            for k in kids:
                if k == 0:
                    cryingKids += 1

            if leftCookies < cryingKids:
                return

            for i in range(len(kids)):
                kids[i] += cookies[index]
                dfs(index+1, kids.copy())
                kids[i] -= cookies[index]
 
        dfs(0, k * [0])
        return self.unfair

        
