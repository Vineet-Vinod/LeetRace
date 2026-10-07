from heapq import heappop, heappush


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        heap: list[tuple[int, int, int, int, int]] = []
        for i, first in enumerate(nums1[:k]):
            second = nums2[0]
            heappush(heap, (first + second, first, second, i, 0))
        pairs: list[list[int]] = []
        while heap and len(pairs) < k:
            _, first, second, i, j = heappop(heap)
            pairs.append([first, second])
            next_j = j + 1
            if next_j < len(nums2):
                next_second = nums2[next_j]
                heappush(
                    heap, (nums1[i] + next_second, nums1[i], next_second, i, next_j)
                )
        return pairs
