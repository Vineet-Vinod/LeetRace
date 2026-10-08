class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        result = heights[:]
        for _ in range(volume):
            position = k
            for direction in (-1, 1):
                current = k
                while (
                    0 <= current + direction < len(result)
                    and result[current + direction] <= result[current]
                ):
                    current += direction
                    if result[current] < result[position]:
                        position = current
                if position != k:
                    break
            result[position] += 1
        return result
