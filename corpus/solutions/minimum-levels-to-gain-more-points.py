class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        scores = [1 if value else -1 for value in possible]
        total = sum(scores)
        prefix = 0
        for index, score in enumerate(scores[:-1]):
            prefix += score
            if prefix > total - prefix:
                return index + 1
        return -1
