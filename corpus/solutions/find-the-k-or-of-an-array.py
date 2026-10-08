class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        result = 0
        for bit in range(32):
            if sum((value >> bit) & 1 for value in nums) >= k:
                result |= 1 << bit
        return result
