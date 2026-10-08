from typing import List


class Solution:
    def beautifulPair(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        best = (10**20, len(nums1), len(nums1))
        for i, point in enumerate(zip(nums1, nums2)):
            if point in seen:
                best = min(best, (0, seen[point], i))
            else:
                seen[point] = i
        if best[0] == 0:
            return list(best[1:])
        points = sorted((x, y, i) for i, (x, y) in enumerate(zip(nums1, nums2)))

        def closest(points):
            nonlocal best
            if len(points) <= 8:
                for a in range(len(points)):
                    for b in range(a + 1, len(points)):
                        x, y, i = points[a]
                        xx, yy, j = points[b]
                        best = min(
                            best, (abs(x - xx) + abs(y - yy), min(i, j), max(i, j))
                        )
                return sorted(points, key=lambda p: p[1])
            mid = len(points) // 2
            split = points[mid][0]
            left = closest(points[:mid])
            right = closest(points[mid:])
            ordered = []
            a = b = 0
            while a < len(left) and b < len(right):
                if left[a][1] <= right[b][1]:
                    ordered.append(left[a])
                    a += 1
                else:
                    ordered.append(right[b])
                    b += 1
            ordered.extend(left[a:])
            ordered.extend(right[b:])
            strip = [p for p in ordered if abs(p[0] - split) <= best[0]]
            for a, (x, y, i) in enumerate(strip):
                b = a + 1
                while b < len(strip) and strip[b][1] - y <= best[0]:
                    xx, yy, j = strip[b]
                    best = min(best, (abs(x - xx) + yy - y, min(i, j), max(i, j)))
                    b += 1
            return ordered

        closest(points)
        return list(best[1:])
