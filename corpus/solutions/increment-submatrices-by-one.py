class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r2 + 1][c1] -= 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c2 + 1] += 1
        answer = [[0] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                above = answer[r - 1][c] if r else 0
                left = answer[r][c - 1] if c else 0
                diagonal = answer[r - 1][c - 1] if r and c else 0
                answer[r][c] = diff[r][c] + above + left - diagonal
        return answer
