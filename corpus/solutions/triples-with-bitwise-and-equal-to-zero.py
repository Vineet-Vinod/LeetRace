class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        counts = Counter(nums)
        pairs = Counter()
        for a, ca in counts.items():
            for b, cb in counts.items():
                pairs[a & b] += ca * cb
        bits = max(nums).bit_length()
        size = 1 << bits
        if len(pairs) * len(counts) <= size * max(1, bits):
            return sum(
                count * frequency
                for pair, count in pairs.items()
                for value, frequency in counts.items()
                if pair & value == 0
            )
        subsets = [0] * size
        for mask, count in pairs.items():
            subsets[mask] = count
        for bit in range(bits):
            step = 1 << bit
            for start in range(0, size, step * 2):
                for mask in range(start + step, start + step * 2):
                    subsets[mask] += subsets[mask - step]
        full = size - 1
        return sum(
            frequency * subsets[full ^ value] for value, frequency in counts.items()
        )
