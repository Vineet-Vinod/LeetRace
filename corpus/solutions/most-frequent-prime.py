class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        counts = Counter()
        directions = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if dr or dc]
        for r in range(rows):
            for c in range(cols):
                for dr, dc in directions:
                    nr, nc = r, c
                    value = 0
                    while 0 <= nr < rows and 0 <= nc < cols:
                        value = value * 10 + mat[nr][nc]
                        if value > 10 and self._is_prime(value):
                            counts[value] += 1
                        nr += dr
                        nc += dc
        return (
            max(
                (
                    value
                    for value, count in counts.items()
                    if count == max(counts.values())
                ),
                default=-1,
            )
            if counts
            else -1
        )

    def _is_prime(self, value: int) -> bool:
        if value < 2:
            return False
        if value % 2 == 0:
            return value == 2
        divisor = 3
        while divisor * divisor <= value:
            if value % divisor == 0:
                return False
            divisor += 2
        return True
