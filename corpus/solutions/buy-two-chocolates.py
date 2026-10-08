class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        first, second = sorted(prices)[:2]
        cost = first + second
        return money - cost if cost <= money else money
