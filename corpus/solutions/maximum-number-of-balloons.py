class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        return min(
            counts.get(char, 0) // (2 if char in "lo" else 1) for char in "balon"
        )
