class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def is_prime(value: int) -> bool:
            if value < 2:
                return False
            divisor = 2
            while divisor * divisor <= value:
                if value % divisor == 0:
                    return False
                divisor += 1
            return True

        prime_indices = [index for index, value in enumerate(nums) if is_prime(value)]
        return prime_indices[-1] - prime_indices[0]
