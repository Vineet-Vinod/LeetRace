class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        size = len(nums)
        best = [size + 1] * (size + 1)
        best[0] = 0
        for end in range(1, size + 1):
            for start in range(end):
                if best[start] <= size and math.gcd(nums[start], nums[end - 1]) > 1:
                    best[end] = min(best[end], best[start] + 1)
        return best[size] if best[size] <= size else -1
