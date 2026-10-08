class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        has_stronger = [False] * n
        for _, weaker in edges:
            has_stronger[weaker] = True
        champions = [team for team, stronger in enumerate(has_stronger) if not stronger]
        return champions[0] if len(champions) == 1 else -1
