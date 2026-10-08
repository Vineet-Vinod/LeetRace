from typing import List


class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        losses = sum(max(cost - cashback, 0) for cost, cashback in transactions)
        return losses + max(min(cost, cashback) for cost, cashback in transactions)
