class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = ["a"] * n
        remaining = k - n
        for index in range(n - 1, -1, -1):
            increase = min(25, remaining)
            result[index] = chr(ord("a") + increase)
            remaining -= increase
        return "".join(result)
