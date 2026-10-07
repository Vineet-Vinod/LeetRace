class Solution:
    def knightDialer(self, n: int) -> int:
        modulo = 10**9 + 7
        moves = (
            (4, 6),
            (6, 8),
            (7, 9),
            (4, 8),
            (0, 3, 9),
            (),
            (0, 1, 7),
            (2, 6),
            (1, 3),
            (2, 4),
        )
        counts = [1] * 10
        for _ in range(n - 1):
            next_counts = [0] * 10
            for digit, destinations in enumerate(moves):
                for destination in destinations:
                    next_counts[destination] += counts[digit]
            counts = [count % modulo for count in next_counts]
        return sum(counts) % modulo
