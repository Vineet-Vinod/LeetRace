class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums = sorted(nums)
        mod = 10**9 + 7
        answer = 0
        power = 1
        for i in range(len(nums)):
            answer = (answer + (nums[i] - nums[-1 - i]) * power) % mod
            power = power * 2 % mod
        return answer
