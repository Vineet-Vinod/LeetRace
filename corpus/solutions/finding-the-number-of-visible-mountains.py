class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        intervals = sorted(
            ((x - y, x + y) for x, y in peaks), key=lambda p: (p[0], -p[1])
        )
        visible = 0
        farthest_right = None
        index = 0
        while index < len(intervals):
            left, right = intervals[index]
            end = index + 1
            while end < len(intervals) and intervals[end] == (left, right):
                end += 1

            if farthest_right is None or right > farthest_right:
                if end - index == 1:
                    visible += 1
                farthest_right = right
            index = end
        return visible
