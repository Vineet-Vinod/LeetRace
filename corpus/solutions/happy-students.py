class Solution:
    def countWays(self, nums: list[int]) -> int:
        nums.sort()
        ways = int(nums[0] > 0) + int(nums[-1] < len(nums))
        for selected in range(1, len(nums)):
            if nums[selected - 1] < selected < nums[selected]:
                ways += 1
        return ways
