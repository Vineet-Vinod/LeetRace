class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        counts: dict[int, int] = {}
        for value in nums:
            counts[value] = counts.get(value, 0) + 1
        maximum = max(counts.values())
        return max(len(nums) % 2, 2 * maximum - len(nums))
