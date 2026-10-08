class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return max((x for x, count in counts.items() if count == 1), default=-1)
