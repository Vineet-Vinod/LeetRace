class Solution:
    def numberOfPoints(self, nums: list[list[int]]) -> int:
        covered: set[int] = set()
        for start, end in nums:
            covered.update(range(start, end + 1))
        return len(covered)
