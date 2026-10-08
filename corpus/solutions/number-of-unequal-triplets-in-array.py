class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        counts = Counter(nums)
        seen = 0
        result = 0
        remaining = len(nums)
        for count in counts.values():
            remaining -= count
            result += seen * count * remaining
            seen += count
        return result
