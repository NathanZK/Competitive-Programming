# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node.right:
                queue.append(node.right)
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)

            if node.left:
                queue.append(node.left)
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)

        queue = deque([target.val])
        visited = set([target.val])
        level = 0

        while queue:
            size = len(queue)
            if level == k:
                return list(queue)
            level += 1

            for _ in range(size):
                node = queue.popleft()

                for child in graph[node]:
                    if child not in visited:
                        queue.append(child)
                        visited.add(child)

        return []