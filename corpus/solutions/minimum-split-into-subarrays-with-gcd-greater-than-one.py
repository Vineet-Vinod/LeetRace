class Solution:
    def minimumSplits(self, nums: List[int]) -> int:
        splits = 1
        common = nums[0]
        for value in nums[1:]:
            next_common = gcd(common, value)
            if next_common == 1:
                splits += 1
                common = value
            else:
                common = next_common
        return splits
