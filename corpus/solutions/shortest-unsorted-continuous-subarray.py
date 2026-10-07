class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        ordered = sorted(nums)
        mismatches = [i for i, (a, b) in enumerate(zip(nums, ordered)) if a != b]
        return 0 if not mismatches else mismatches[-1] - mismatches[0] + 1
