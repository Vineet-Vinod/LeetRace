class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        ordered = sorted(score, reverse=True)
        labels = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        ranks = {
            value: labels[index] if index < 3 else str(index + 1)
            for index, value in enumerate(ordered)
        }
        return [ranks[value] for value in score]
