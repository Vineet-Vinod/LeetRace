class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        frequencies: Dict[int, int] = {}
        pairs = 0
        for value in nums:
            difference = value - int(str(value)[::-1])
            pairs = (pairs + frequencies.get(difference, 0)) % (10**9 + 7)
            frequencies[difference] = frequencies.get(difference, 0) + 1
        return pairs
