class Solution:
    def maxIntersectionCount(self, y: list[int]) -> int:
        events = {}

        def add(x, delta):
            events[x] = events.get(x, 0) + delta

        # Each segment includes its left endpoint; only the last includes its right.
        for i, (a, b) in enumerate(zip(y, y[1:])):
            a *= 2
            b *= 2
            if i != len(y) - 2:
                b += -1 if b > a else 1
            lo, hi = sorted((a, b))
            add(lo, 1)
            add(hi + 1, -1)
        total = answer = 0
        for x in sorted(events):
            total += events[x]
            answer = max(answer, total)
        return answer
