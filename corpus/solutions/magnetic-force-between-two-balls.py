class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        ordered = sorted(position)
        low, high = 1, (ordered[-1] - ordered[0]) // (m - 1)
        answer = 0
        while low <= high:
            distance = (low + high) // 2
            placed = 1
            last = ordered[0]
            for point in ordered[1:]:
                if point - last >= distance:
                    placed += 1
                    last = point
            if placed >= m:
                answer = distance
                low = distance + 1
            else:
                high = distance - 1
        return answer
