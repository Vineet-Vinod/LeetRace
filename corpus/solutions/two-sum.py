from bisect import bisect_right


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        positions: dict[int, list[int]] = {}
        for index, value in enumerate(nums):
            positions.setdefault(value, []).append(index)
        for index, value in enumerate(nums):
            matches = positions.get(target - value, [])
            offset = bisect_right(matches, index)
            if offset < len(matches):
                return [index, matches[offset]]
        return []
