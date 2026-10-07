class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        sums = [[0] * cols for _ in range(rows)]
        counts = [[0] * cols for _ in range(rows)]
        for top in range(rows - 2):
            for left in range(cols - 2):
                valid = True
                for r in range(top, top + 3):
                    for c in range(left, left + 3):
                        if (
                            r < top + 2
                            and abs(image[r][c] - image[r + 1][c]) > threshold
                        ):
                            valid = False
                        if (
                            c < left + 2
                            and abs(image[r][c] - image[r][c + 1]) > threshold
                        ):
                            valid = False
                if valid:
                    average = (
                        sum(
                            image[r][c]
                            for r in range(top, top + 3)
                            for c in range(left, left + 3)
                        )
                        // 9
                    )
                    for r in range(top, top + 3):
                        for c in range(left, left + 3):
                            sums[r][c] += average
                            counts[r][c] += 1
        return [
            [
                sums[r][c] // counts[r][c] if counts[r][c] else image[r][c]
                for c in range(cols)
            ]
            for r in range(rows)
        ]
