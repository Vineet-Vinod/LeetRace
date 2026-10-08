class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        ordered = sorted(nums)
        result = []
        for index in range(0, len(ordered), 2):
            result.extend([ordered[index + 1], ordered[index]])
        return result
