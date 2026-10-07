class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        radius = [0] * n
        left, right = 0, -1
        for i in range(n):
            k = 1 if i > right else min(radius[left + right - i], right - i + 1)
            while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
                k += 1
            radius[i] = k
            if i + k - 1 > right:
                left, right = i - k + 1, i + k - 1
        ending = [1] * n
        starting = [1] * n
        for i, r in enumerate(radius):
            length = 2 * r - 1
            ending[i + r - 1] = max(ending[i + r - 1], length)
            starting[i - r + 1] = max(starting[i - r + 1], length)
        for i in range(n - 2, -1, -1):
            ending[i] = max(ending[i], ending[i + 1] - 2)
        for i in range(1, n):
            starting[i] = max(starting[i], starting[i - 1] - 2)
            ending[i] = max(ending[i], ending[i - 1])
        for i in range(n - 2, -1, -1):
            starting[i] = max(starting[i], starting[i + 1])
        return max(ending[i] * starting[i + 1] for i in range(n - 1))
