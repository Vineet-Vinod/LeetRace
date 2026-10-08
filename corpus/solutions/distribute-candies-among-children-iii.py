class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        answer = 0
        for excluded, coefficient in enumerate((1, -3, 3, -1)):
            remaining = n - excluded * (limit + 1)
            if remaining >= 0:
                answer += coefficient * (remaining + 1) * (remaining + 2) // 2
        return answer
