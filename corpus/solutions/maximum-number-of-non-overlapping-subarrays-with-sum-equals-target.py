class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        prefix = 0
        seen = {0}
        count = 0
        for value in nums:
            prefix += value
            if prefix - target in seen:
                count += 1
                prefix = 0
                seen = {0}
            else:
                seen.add(prefix)
        return count
