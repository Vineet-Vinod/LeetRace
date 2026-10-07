class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        size = len(matrix)
        low, high = matrix[0][0], matrix[-1][-1]
        while low < high:
            middle = (low + high) // 2
            count = col = 0
            for row in range(size - 1, -1, -1):
                while col < size and matrix[row][col] <= middle:
                    col += 1
                count += col
            if count < k:
                low = middle + 1
            else:
                high = middle
        return low
