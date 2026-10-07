class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        remainder = sum(nums) % p
        if remainder == 0:
            return 0
        last = {0: -1}
        prefix = 0
        best = len(nums)
        for i, value in enumerate(nums):
            prefix = (prefix + value) % p
            wanted = (prefix - remainder) % p
            if wanted in last:
                best = min(best, i - last[wanted])
            last[prefix] = i
        return -1 if best == len(nums) else best
