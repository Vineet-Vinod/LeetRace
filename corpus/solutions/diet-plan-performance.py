class Solution:
    def dietPlanPerformance(
        self, calories: List[int], k: int, lower: int, upper: int
    ) -> int:
        score = 0
        window = sum(calories[:k])
        for start in range(len(calories) - k + 1):
            if window < lower:
                score -= 1
            elif window > upper:
                score += 1
            if start + k < len(calories):
                window += calories[start + k] - calories[start]
        return score
