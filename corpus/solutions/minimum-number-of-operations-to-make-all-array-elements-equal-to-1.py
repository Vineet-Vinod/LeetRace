class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ones = nums.count(1)
        if ones:
            return len(nums) - ones
        best = len(nums) + 1
        for left in range(len(nums)):
            value = nums[left]
            for right in range(left + 1, len(nums)):
                value = math.gcd(value, nums[right])
                if value == 1:
                    best = min(best, right - left + 1)
                    break
        return -1 if best == len(nums) + 1 else best - 1 + len(nums) - 1
