class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        suffix = [0] * (len(nums) + 1)
        seen: set[int] = set()
        for index in range(len(nums) - 1, -1, -1):
            seen.add(nums[index])
            suffix[index] = len(seen)
        prefix: set[int] = set()
        result: list[int] = []
        for index, value in enumerate(nums):
            prefix.add(value)
            result.append(len(prefix) - suffix[index + 1])
        return result
