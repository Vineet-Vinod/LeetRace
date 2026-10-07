class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for bit in range(32):
            count = sum((value >> bit) & 1 for value in nums) % 3
            result |= count << bit
        return result - (1 << 32) if result >= (1 << 31) else result
