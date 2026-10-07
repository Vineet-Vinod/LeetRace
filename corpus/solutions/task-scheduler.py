class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        highest = max(counts.values())
        tied = sum(count == highest for count in counts.values())
        return max(len(tasks), (highest - 1) * (n + 1) + tied)
