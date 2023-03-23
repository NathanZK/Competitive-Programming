class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        transfer = [0] * n
        achievable = 0

        def dfs(index, accepted):
            nonlocal achievable

            if index == len(requests):
                if transfer.count(0) == len(transfer):
                    achievable = max(achievable, accepted)

                return

            dfs(index+1, accepted)
            from_, to_ = requests[index]

            transfer[from_] -= 1
            transfer[to_] += 1

            dfs(index+1, accepted + 1)

            transfer[from_] += 1
            transfer[to_] -= 1

        dfs(0, 0)
        return achievable

        
