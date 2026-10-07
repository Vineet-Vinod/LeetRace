from typing import List


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        total = row * col
        parent = list(range(total + 2))
        size = [1] * (total + 2)
        land = [False] * total

        def find(i):
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i

        def merge(a, b):
            a, b = find(a), find(b)
            if a != b:
                if size[a] < size[b]:
                    a, b = b, a
                parent[b] = a
                size[a] += size[b]

        for day in range(total - 1, -1, -1):
            r, c = cells[day][0] - 1, cells[day][1] - 1
            i = r * col + c
            land[i] = True
            if r == 0:
                merge(i, total)
            if r == row - 1:
                merge(i, total + 1)
            for rr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= rr < row and 0 <= cc < col and land[rr * col + cc]:
                    merge(i, rr * col + cc)
            if find(total) == find(total + 1):
                return day
        return 0
