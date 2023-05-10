class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        incoming = Counter()
        createdRecipes = []
        queue = deque(supplies)

        for n in range(len(ingredients)):
            for ing in ingredients[n]:
                graph[ing].append(recipes[n])

            incoming[recipes[n]] = len(ingredients[n])

        recipes = set(recipes)
        while queue:
            rec = queue.popleft()
            if rec in recipes:
                createdRecipes.append(rec)

            for neighbor in graph[rec]:
                incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    queue.append(neighbor)

        return createdRecipes