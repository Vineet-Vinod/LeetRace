class Solution:
    def countPalindromes(self, s: str) -> int:
        mod = 10**9 + 7
        left = [0] * 10
        right = [0] * 10
        lp = [[0] * 10 for _ in range(10)]
        rp = [[0] * 10 for _ in range(10)]
        for ch in reversed(s):
            x = int(ch)
            for y in range(10):
                rp[x][y] += right[y]
            right[x] += 1
        answer = 0
        for ch in s:
            x = int(ch)
            right[x] -= 1
            for y in range(10):
                rp[x][y] -= right[y]
            answer += sum(lp[a][b] * rp[b][a] for a in range(10) for b in range(10))
            answer %= mod
            for y in range(10):
                lp[y][x] += left[y]
            left[x] += 1
        return answer
