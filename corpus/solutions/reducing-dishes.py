class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        total = answer = 0
        for value in sorted(satisfaction, reverse=True):
            if total + value <= 0:
                break
            total += value
            answer += total
        return answer
