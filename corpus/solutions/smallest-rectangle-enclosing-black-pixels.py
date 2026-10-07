class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        m, n = len(image), len(image[0])

        def bound(low, high, predicate, present):
            while low < high:
                mid = (low + high) // 2
                if predicate(mid) == present:
                    high = mid
                else:
                    low = mid + 1
            return low

        def row(i):
            return "1" in image[i]

        def col(j):
            return any(image[i][j] == "1" for i in range(m))

        top = bound(0, x, row, True)
        bottom = bound(x + 1, m, row, False)
        left = bound(0, y, col, True)
        right = bound(y + 1, n, col, False)
        return (bottom - top) * (right - left)
