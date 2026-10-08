class Solution:
    def countVowelStrings(self, n: int) -> int:
        counts = [1] * 5
        for _ in range(n - 1):
            for index in range(3, -1, -1):
                counts[index] += counts[index + 1]
        return sum(counts)
