class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [list(values) for values in combinations(range(1, n + 1), k)]
