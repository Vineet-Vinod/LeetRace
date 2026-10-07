class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        blocks = [word[i : i + k] for i in range(0, len(word), k)]
        counts = Counter(blocks)
        return len(blocks) - max(counts.values())
