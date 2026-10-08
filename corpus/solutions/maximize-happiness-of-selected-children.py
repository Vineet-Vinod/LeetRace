class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        return sum(
            max(0, value - turn)
            for turn, value in enumerate(sorted(happiness, reverse=True)[:k])
        )
