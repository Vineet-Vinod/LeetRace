class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        result = 0
        total = sum(nums)
        for value in nums:
            result |= value
        bit = 0
        while (1 << bit) <= total:
            if sum(value % (1 << (bit + 1)) for value in nums) >= (1 << bit):
                result |= 1 << bit
            bit += 1
        return result
