class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        horizontal = [1] + hFences + [m]
        vertical = [1] + vFences + [n]
        horizontal_lengths = set()
        for i, left in enumerate(horizontal):
            for right in horizontal[i + 1 :]:
                horizontal_lengths.add(right - left)
        best = 0
        for i, left in enumerate(vertical):
            for right in vertical[i + 1 :]:
                length = right - left
                if length in horizontal_lengths:
                    best = max(best, length)
        return best * best % (10**9 + 7) if best else -1
