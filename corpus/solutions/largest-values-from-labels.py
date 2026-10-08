class Solution:
    def largestValsFromLabels(
        self, values: List[int], labels: List[int], numWanted: int, useLimit: int
    ) -> int:
        items = sorted(zip(values, labels), reverse=True)
        used: dict[int, int] = {}
        total = 0
        selected = 0
        for value, label in items:
            if used.get(label, 0) >= useLimit:
                continue
            total += value
            selected += 1
            used[label] = used.get(label, 0) + 1
            if selected == numWanted:
                break
        return total
