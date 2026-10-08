class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        return min(
            divisors,
            key=lambda divisor: (-sum(value % divisor == 0 for value in nums), divisor),
        )
