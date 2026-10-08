class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        [row.count("B") for row in picture]
        patterns = Counter(tuple(row) for row in picture)
        col_counts = [
            sum(row[col] == "B" for row in picture) for col in range(len(picture[0]))
        ]
        answer = 0
        for row_pattern, count in patterns.items():
            if count != target or row_pattern.count("B") != target:
                continue
            answer += (
                sum(
                    pixel == "B" and col_counts[col] == target
                    for col, pixel in enumerate(row_pattern)
                )
                * target
            )
        return answer
