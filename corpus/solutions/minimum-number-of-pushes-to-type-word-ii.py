class Solution:
    def minimumPushes(self, word: str) -> int:
        frequencies = sorted(Counter(word).values(), reverse=True)
        return sum(count * (index // 8 + 1) for index, count in enumerate(frequencies))
