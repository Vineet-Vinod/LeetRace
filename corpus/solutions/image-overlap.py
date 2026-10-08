class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        first = [(r, c) for r in range(n) for c in range(n) if img1[r][c]]
        second = [(r, c) for r in range(n) for c in range(n) if img2[r][c]]
        offsets = Counter((r2 - r1, c2 - c1) for r1, c1 in first for r2, c2 in second)
        return max(offsets.values(), default=0)
