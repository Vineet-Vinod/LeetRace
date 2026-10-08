class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        ordered = sorted(nums)
        matched = 0
        for value in ordered:
            if value > ordered[matched]:
                matched += 1
        return matched
