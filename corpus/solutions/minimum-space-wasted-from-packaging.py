from bisect import bisect_right


class Solution:
    def minWastedSpace(self, packages: list[int], boxes: list[list[int]]) -> int:
        packages = sorted(packages)
        best = 10**30
        for supplier in boxes:
            supplier = sorted(supplier)
            if supplier[-1] < packages[-1]:
                continue
            previous = total = 0
            for size in supplier:
                end = bisect_right(packages, size)
                total += (end - previous) * size
                previous = end
            best = min(best, total - sum(packages))
        return -1 if best == 10**30 else best % 1_000_000_007
