class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if len(matrix) > len(matrix[0]):
            matrix = list(zip(*matrix))
        height, width = len(matrix), len(matrix[0])
        answer = -(10**30)
        for top in range(height):
            sums = [0] * width
            for bottom in range(top, height):
                sums = [a + b for a, b in zip(sums, matrix[bottom])]
                prefixes = [0]
                total = 0
                for value in sums:
                    total += value
                    index = bisect_left(prefixes, total - k)
                    if index < len(prefixes):
                        answer = max(answer, total - prefixes[index])
                        if answer == k:
                            return k
                    insort(prefixes, total)
        return answer
