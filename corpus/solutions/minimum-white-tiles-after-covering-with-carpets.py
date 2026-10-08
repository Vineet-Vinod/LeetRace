class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        if numCarpets * carpetLen >= n:
            return 0
        previous = [0] * (n + 1)
        for i, c in enumerate(floor, 1):
            previous[i] = previous[i - 1] + int(c)
        for _ in range(numCarpets):
            current = [0] * (n + 1)
            for i, c in enumerate(floor, 1):
                current[i] = min(
                    current[i - 1] + int(c), previous[max(0, i - carpetLen)]
                )
            previous = current
        return previous[n]
