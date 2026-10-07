from typing import List


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance = [0] * 12
        for a, b, amount in transactions:
            balance[a] -= amount
            balance[b] += amount
        debts = [x for x in balance if x]

        def settle(start):
            while start < len(debts) and not debts[start]:
                start += 1
            if start == len(debts):
                return 0
            best = len(debts)
            tried = set()
            for j in range(start + 1, len(debts)):
                if debts[start] * debts[j] >= 0 or debts[j] in tried:
                    continue
                tried.add(debts[j])
                old = debts[j]
                debts[j] += debts[start]
                best = min(best, 1 + settle(start + 1))
                debts[j] = old
                if old + debts[start] == 0:
                    break
            return best

        return settle(0)
