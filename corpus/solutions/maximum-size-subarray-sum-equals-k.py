class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        earliest = {0: -1}
        prefix = best = 0
        for index, value in enumerate(nums):
            prefix += value
            if prefix - k in earliest:
                best = max(best, index - earliest[prefix - k])
            earliest.setdefault(prefix, index)
        return best
