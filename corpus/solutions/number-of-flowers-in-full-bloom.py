from bisect import bisect_left, bisect_right


class Solution:
    def fullBloomFlowers(
        self, flowers: list[list[int]], people: list[int]
    ) -> list[int]:
        starts = sorted(a for a, b in flowers)
        ends = sorted(b for a, b in flowers)
        return [bisect_right(starts, p) - bisect_left(ends, p) for p in people]
