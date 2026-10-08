class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        for length in range(2, 10):
            for start in range(1, 11 - length):
                value = int(
                    "".join(str(digit) for digit in range(start, start + length))
                )
                if low <= value <= high:
                    result.append(value)
        return sorted(result)
