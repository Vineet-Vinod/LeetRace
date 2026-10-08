class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(value: int) -> bool:
            if value < 2:
                return False
            for divisor in range(2, math.isqrt(value) + 1):
                if value % divisor == 0:
                    return False
            return True

        n = len(nums)
        return max(
            (
                nums[i][j]
                for i in range(n)
                for j in {i, n - 1 - i}
                if is_prime(nums[i][j])
            ),
            default=0,
        )
