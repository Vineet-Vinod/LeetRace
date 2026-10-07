class Solution:
    def countEven(self, num: int) -> int:
        def even_digit_sum(value: int) -> bool:
            return sum(map(int, str(value))) % 2 == 0

        return sum(even_digit_sum(value) for value in range(1, num + 1))
