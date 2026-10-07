class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        result = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                values = [
                    img[nr][nc]
                    for nr in range(max(0, r - 1), min(rows, r + 2))
                    for nc in range(max(0, c - 1), min(cols, c + 2))
                ]
                result[r][c] = sum(values) // len(values)
        return result
