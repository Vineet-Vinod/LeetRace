class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        ending: dict[int, list[tuple[int, int]]] = {}
        for start, end, tip in rides:
            ending.setdefault(end, []).append((start, end - start + tip))
        best = [0] * (n + 1)
        for point in range(1, n + 1):
            best[point] = best[point - 1]
            for start, earning in ending.get(point, []):
                best[point] = max(best[point], best[start] + earning)
        return best[n]
