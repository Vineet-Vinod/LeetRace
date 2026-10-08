class Solution:
    def findMissingRanges(
        self, nums: List[int], lower: int, upper: int
    ) -> List[List[int]]:
        result: list[list[int]] = []
        next_value = lower
        for value in nums:
            if next_value < value:
                result.append([next_value, value - 1])
            next_value = value + 1
        if next_value <= upper:
            result.append([next_value, upper])
        return result
