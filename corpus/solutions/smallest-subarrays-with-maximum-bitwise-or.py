class Solution:
    def smallestSubarrays(self, nums: list[int]) -> list[int]:
        last_seen = [-1] * 31
        result = [1] * len(nums)
        for index in range(len(nums) - 1, -1, -1):
            for bit in range(31):
                if nums[index] & (1 << bit):
                    last_seen[bit] = index
            furthest = max(
                (position for position in last_seen if position >= 0), default=index
            )
            result[index] = furthest - index + 1
        return result
