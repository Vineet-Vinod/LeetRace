class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        blocked: dict[int, int] = {}
        for row, seat in reservedSeats:
            blocked[row] = (
                blocked.get(row, 0) | (1 << (seat - 2))
                if 2 <= seat <= 9
                else blocked.get(row, 0)
            )
        left, middle, right = 0b00001111, 0b00111100, 0b11110000
        families = 2 * (n - len(blocked))
        for mask in blocked.values():
            if mask & left == 0 or mask & right == 0:
                families += 1
            elif mask & middle == 0:
                families += 1
        return families
