from typing import List


class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        trees = [[0] * 5001 for _ in range(2)]

        def query(tree: List[int], index: int) -> int:
            value = 0
            while index:
                value = max(value, tree[index])
                index -= index & -index
            return value

        def update(tree: List[int], index: int, value: int) -> None:
            while index <= 5000:
                tree[index] = max(tree[index], value)
                index += index & -index

        answer = -1
        for price, profit in zip(prices, profits):
            pair = query(trees[1], price - 1)
            single = query(trees[0], price - 1)
            if pair:
                answer = max(answer, pair + profit)
            if single:
                update(trees[1], price, single + profit)
            update(trees[0], price, profit)
        return answer
