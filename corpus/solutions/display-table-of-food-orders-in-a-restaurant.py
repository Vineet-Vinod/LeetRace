from collections import Counter, defaultdict


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = sorted({food for _, _, food in orders})
        tables: dict[int, Counter[str]] = defaultdict(Counter)
        for _, table, food in orders:
            tables[int(table)][food] += 1
        result = [["Table", *foods]]
        for table in sorted(tables):
            result.append([str(table), *(str(tables[table][food]) for food in foods)])
        return result
