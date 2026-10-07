class Solution:
    def totalNQueens(self, n: int) -> int:
        full = (1 << n) - 1

        def search(columns, left, right):
            if columns == full:
                return 1
            available = full & ~(columns | left | right)
            answer = 0
            while available:
                bit = available & -available
                available -= bit
                answer += search(columns | bit, (left | bit) << 1, (right | bit) >> 1)
            return answer

        return search(0, 0, 0)
