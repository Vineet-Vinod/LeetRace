class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best_left = values[0]
        answer = -(10**18)
        for j in range(1, len(values)):
            answer = max(answer, best_left + values[j] - j)
            best_left = max(best_left, values[j] + j)
        return answer
