from array import array


class Solution:
    def numberOfCombinations(self, num: str) -> int:
        n = len(num)
        if num[0] == "0":
            return 0
        mod = 1000000007
        lcp = [array("H", [0]) * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if num[i] == num[j]:
                    lcp[i][j] = 1 + lcp[i + 1][j + 1]
        dp = [array("I", [0]) * (n + 1) for _ in range(n + 1)]
        for end in range(1, n + 1):
            row = dp[end]
            for size in range(1, end + 1):
                start = end - size
                ways = 0
                if num[start] != "0":
                    if start == 0:
                        ways = 1
                    else:
                        ways = dp[start][min(size - 1, start)]
                        if start >= size:
                            common = lcp[start - size][start]
                            if (
                                common >= size
                                or num[start - size + common] <= num[start + common]
                            ):
                                ways = dp[start][size]
                row[size] = (row[size - 1] + ways) % mod
        return dp[n][n]
