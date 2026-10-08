class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        {recipe: i for i, recipe in enumerate(recipes)}
        dependents: Dict[str, List[int]] = defaultdict(list)
        missing = [len(items) for items in ingredients]
        for i, items in enumerate(ingredients):
            for item in items:
                dependents[item].append(i)
        queue = deque(supplies)
        available = set(supplies)
        made = set()
        while queue:
            item = queue.popleft()
            for index in dependents[item]:
                missing[index] -= 1
                if missing[index] == 0:
                    recipe = recipes[index]
                    if recipe not in available:
                        available.add(recipe)
                        made.add(recipe)
                        queue.append(recipe)
        return sorted(made)
