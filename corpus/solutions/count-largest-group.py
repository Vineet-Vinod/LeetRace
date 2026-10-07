class Solution:
    def countLargestGroup(self, n: int) -> int:
        counts = Counter(sum(map(int, str(value))) for value in range(1, n + 1))
        largest = max(counts.values())
        return sum(size == largest for size in counts.values())
