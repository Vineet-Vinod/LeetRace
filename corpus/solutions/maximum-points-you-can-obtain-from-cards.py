class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window = len(cardPoints) - k
        if window == 0:
            return sum(cardPoints)
        current = sum(cardPoints[:window])
        minimum = current
        for i in range(window, len(cardPoints)):
            current += cardPoints[i] - cardPoints[i - window]
            minimum = min(minimum, current)
        return sum(cardPoints) - minimum
