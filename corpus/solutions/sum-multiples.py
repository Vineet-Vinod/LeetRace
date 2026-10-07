class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return sum(
            value
            for value in range(1, n + 1)
            if value % 3 == 0 or value % 5 == 0 or value % 7 == 0
        )
