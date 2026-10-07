class Solution:
    def minimumLines(self, points: List[List[int]]) -> int:
        n = len(points)
        lines = []
        for i in range(n):
            for j in range(i + 1, n):
                mask = 0
                x1, y1 = points[i]
                x2, y2 = points[j]
                for k, (x, y) in enumerate(points):
                    if (x2 - x1) * (y - y1) == (y2 - y1) * (x - x1):
                        mask |= 1 << k
                lines.append(mask)
        lines.extend(1 << i for i in range(n))
        full = (1 << n) - 1
        dp = [n + 1] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            if dp[mask] > n:
                continue
            remaining = full ^ mask
            if not remaining:
                continue
            first = (remaining & -remaining).bit_length() - 1
            for line in lines:
                if line >> first & 1:
                    next_mask = mask | line
                    dp[next_mask] = min(dp[next_mask], dp[mask] + 1)
        return dp[full]
