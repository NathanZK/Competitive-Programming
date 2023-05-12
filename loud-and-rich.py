class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        richerPeople = [set() for _ in range(len(quiet))]
        queue = deque()
        incoming = Counter()
        quietest = [0 for _ in range(len(quiet))]

        for rich, poor in richer:
            graph[rich].append(poor)
            incoming[poor] += 1

        for node in range(len(quiet)):
            if incoming[node] == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()

            for neighbor in graph[node]:
                richerPeople[neighbor].add(node)
                richerPeople[neighbor].update(richerPeople[node])
                incoming[neighbor] -= 1

                if incoming[neighbor] == 0:
                    richerPeople[neighbor].add(neighbor)
                    queue.append(neighbor)

        for i in range(len(quietest)):
            if len(richerPeople[i]) == 0:
                quietest[i] = i
            else:
                quietest[i] = min(richerPeople[i], key = lambda x: quiet[x])

        return quietest