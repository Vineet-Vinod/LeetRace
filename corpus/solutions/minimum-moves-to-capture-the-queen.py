class Solution:
    def minMovesToCaptureTheQueen(
        self, a: int, b: int, c: int, d: int, e: int, f: int
    ) -> int:
        rook_attacks = a == e and (b == f or not (a == c and min(b, f) < d < max(b, f)))
        rook_attacks |= b == f and (
            a == e or not (b == d and min(a, e) < c < max(a, e))
        )
        if rook_attacks:
            return 1
        bishop_attacks = abs(c - e) == abs(d - f)
        bishop_blocked = (
            (a - c) * (f - d) == (e - c) * (b - d)
            and min(c, e) < a < max(c, e)
            and min(d, f) < b < max(d, f)
        )
        if bishop_attacks and not bishop_blocked:
            return 1
        return 2
