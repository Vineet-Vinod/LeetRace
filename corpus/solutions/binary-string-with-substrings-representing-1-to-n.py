class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for value in range(n, n // 2, -1):
            if bin(value)[2:] not in s:
                return False
        return True
