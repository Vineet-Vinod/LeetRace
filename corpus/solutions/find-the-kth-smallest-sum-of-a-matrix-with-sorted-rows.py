from heapq import heappop, heappush


class Solution:
    def kthSmallest(self, mat: list[list[int]], k: int) -> int:
        sums = [0]
        for row in mat:
            heap = [(s + row[0], i, 0) for i, s in enumerate(sums)]
            from heapq import heapify

            heapify(heap)
            merged = []
            while heap and len(merged) < k:
                value, i, j = heappop(heap)
                merged.append(value)
                if j + 1 < len(row):
                    heappush(heap, (sums[i] + row[j + 1], i, j + 1))
            sums = merged
        return sums[k - 1]
