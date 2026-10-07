class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        from collections import Counter

        counts = Counter(nums)
        duplicate = next(value for value, count in counts.items() if count == 2)
        missing = next(
            value for value in range(1, len(nums) + 1) if value not in counts
        )
        return [duplicate, missing]
