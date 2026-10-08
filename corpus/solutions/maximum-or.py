class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] | nums[i]
        prefix = answer = 0
        for i, value in enumerate(nums):
            answer = max(answer, prefix | (value << k) | suffix[i + 1])
            prefix |= value
        return answer
