from functools import cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def solve(i: int, remaining: int) -> int:
            if len(s) - i <= remaining:
                return 0
            best = solve(i + 1, remaining - 1) if remaining else 10**9
            count = deleted = 0
            for j in range(i, len(s)):
                if s[j] == s[i]:
                    count += 1
                else:
                    deleted += 1
                    if deleted > remaining:
                        break
                cost = 1 + (len(str(count)) if count > 1 else 0)
                best = min(best, cost + solve(j + 1, remaining - deleted))
            return best

        return solve(0, k)
