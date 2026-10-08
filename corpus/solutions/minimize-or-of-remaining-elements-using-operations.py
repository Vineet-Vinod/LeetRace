class Solution:
    def minOrAfterOperations(self, nums: list[int], k: int) -> int:
        zero_bits = answer = 0
        for bit in range(29, -1, -1):
            mask = zero_bits | (1 << bit)
            current = mask
            groups = 0
            for value in nums:
                current &= value
                if current == 0:
                    groups += 1
                    current = mask
            if len(nums) - groups <= k:
                zero_bits = mask
            else:
                answer |= 1 << bit
        return answer
