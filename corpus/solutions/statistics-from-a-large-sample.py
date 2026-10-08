class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        total_count = sum(count)
        total_sum = sum(value * frequency for value, frequency in enumerate(count))
        minimum = next(value for value, frequency in enumerate(count) if frequency)
        maximum = next(value for value in range(255, -1, -1) if count[value])
        mode = max(range(256), key=lambda value: count[value])
        middle_ranks = ((total_count - 1) // 2, total_count // 2)
        seen = 0
        middle_values = []
        for value, frequency in enumerate(count):
            for rank in middle_ranks:
                if seen <= rank < seen + frequency:
                    middle_values.append(value)
            seen += frequency
        median = sum(middle_values) / 2
        return [
            float(minimum),
            float(maximum),
            total_sum / total_count,
            median,
            float(mode),
        ]
