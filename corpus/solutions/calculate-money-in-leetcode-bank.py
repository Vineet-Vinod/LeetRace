class Solution:
    def totalMoney(self, n: int) -> int:
        weeks, days = divmod(n, 7)
        return (
            28 * weeks
            + 7 * weeks * (weeks - 1) // 2
            + days * (weeks + 1)
            + days * (days - 1) // 2
        )
