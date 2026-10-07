class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        counts = [0] * 24
        answer = 0
        for hour in hours:
            remainder = hour % 24
            answer += counts[(-remainder) % 24]
            counts[remainder] += 1
        return answer
