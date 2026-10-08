class Solution:
    def countBlackBlocks(
        self, m: int, n: int, coordinates: List[List[int]]
    ) -> List[int]:
        counts: Dict[Tuple[int, int], int] = {}
        for row, col in coordinates:
            for top in (row - 1, row):
                for left in (col - 1, col):
                    if 0 <= top < m - 1 and 0 <= left < n - 1:
                        counts[(top, left)] = counts.get((top, left), 0) + 1
        answer = [0] * 5
        answer[0] = (m - 1) * (n - 1) - len(counts)
        for black_count in counts.values():
            answer[black_count] += 1
        return answer
