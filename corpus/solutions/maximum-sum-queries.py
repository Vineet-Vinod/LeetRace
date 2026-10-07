from typing import List
from bisect import bisect_left


class Solution:
    def maximumSumQueries(
        self, nums1: List[int], nums2: List[int], queries: List[List[int]]
    ) -> List[int]:
        ys = sorted(set(nums2))
        tree = [-1] * (len(ys) + 1)
        points = sorted(zip(nums1, nums2), reverse=True)
        answer = [-1] * len(queries)
        j = 0
        for x, y, i in sorted(
            ((x, y, i) for i, (x, y) in enumerate(queries)), reverse=True
        ):
            while j < len(points) and points[j][0] >= x:
                a, b = points[j]
                j += 1
                index = len(ys) - bisect_left(ys, b)
                while index < len(tree):
                    tree[index] = max(tree[index], a + b)
                    index += index & -index
            index = len(ys) - bisect_left(ys, y)
            best = -1
            while index:
                best = max(best, tree[index])
                index -= index & -index
            answer[i] = best
        return answer
