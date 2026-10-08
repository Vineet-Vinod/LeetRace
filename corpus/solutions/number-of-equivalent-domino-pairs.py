class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts: dict[tuple[int, int], int] = {}
        pairs = 0
        for first, second in dominoes:
            key = (min(first, second), max(first, second))
            pairs += counts.get(key, 0)
            counts[key] = counts.get(key, 0) + 1
        return pairs
