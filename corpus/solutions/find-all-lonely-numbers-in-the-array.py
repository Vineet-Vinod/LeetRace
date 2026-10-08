class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        return sorted(
            value
            for value, count in counts.items()
            if count == 1 and value - 1 not in counts and value + 1 not in counts
        )
