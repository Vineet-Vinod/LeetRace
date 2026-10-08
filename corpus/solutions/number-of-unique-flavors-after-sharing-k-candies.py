class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        remaining = Counter(candies)
        distinct = len(remaining)
        for flavor in candies[:k]:
            remaining[flavor] -= 1
            if remaining[flavor] == 0:
                distinct -= 1
        best = distinct
        for right in range(k, len(candies)):
            flavor_out = candies[right - k]
            remaining[flavor_out] += 1
            if remaining[flavor_out] == 1:
                distinct += 1
            flavor_in = candies[right]
            remaining[flavor_in] -= 1
            if remaining[flavor_in] == 0:
                distinct -= 1
            best = max(best, distinct)
        return best
