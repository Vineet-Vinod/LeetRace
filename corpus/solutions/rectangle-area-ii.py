from typing import List
from collections import Counter


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.extend([(x1, 1, y1, y2), (x2, -1, y1, y2)])
        events.sort()
        active = Counter()
        previous = events[0][0]
        area = 0
        for x, delta, y1, y2 in events:
            length = 0
            end = -1
            for (low, high), count in sorted(active.items()):
                if count:
                    length += max(0, high - max(end, low))
                    end = max(end, high)
            area += (x - previous) * length
            previous = x
            active[y1, y2] += delta
        return area % (10**9 + 7)
