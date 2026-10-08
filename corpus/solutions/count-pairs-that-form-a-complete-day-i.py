class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        remainders: dict[int, int] = {}
        pairs = 0
        for hour in hours:
            remainder = hour % 24
            pairs += remainders.get((-remainder) % 24, 0)
            remainders[remainder] = remainders.get(remainder, 0) + 1
        return pairs
