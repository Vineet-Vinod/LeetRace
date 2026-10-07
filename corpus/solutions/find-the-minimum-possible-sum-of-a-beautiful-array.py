class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        small_count = min(n, target // 2)
        answer = small_count * (small_count + 1) // 2
        remaining = n - small_count
        first_large = target
        answer += remaining * (2 * first_large + remaining - 1) // 2
        return answer
