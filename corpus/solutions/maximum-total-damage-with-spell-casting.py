class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counts = Counter(power)
        values = sorted(counts)
        best = [0] * (len(values) + 1)
        for i, value in enumerate(values, start=1):
            previous = i - 1
            while previous > 0 and values[previous - 1] >= value - 2:
                previous -= 1
            best[i] = max(best[i - 1], best[previous] + value * counts[value])
        return best[-1]
