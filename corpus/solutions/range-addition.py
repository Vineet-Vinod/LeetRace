class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        difference = [0] * (length + 1)
        for start, end, increment in updates:
            difference[start] += increment
            difference[end + 1] -= increment
        result: list[int] = []
        current = 0
        for value in difference[:length]:
            current += value
            result.append(current)
        return result
