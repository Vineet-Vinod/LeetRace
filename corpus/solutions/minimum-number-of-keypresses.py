class Solution:
    def minimumKeypresses(self, s: str) -> int:
        frequencies = sorted(Counter(s).values(), reverse=True)
        return sum(
            (index // 9 + 1) * frequency for index, frequency in enumerate(frequencies)
        )
