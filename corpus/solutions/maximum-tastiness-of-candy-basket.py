class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        ordered = sorted(price)
        low, high = 0, ordered[-1] - ordered[0]
        best = 0
        while low <= high:
            distance = (low + high) // 2
            count = 1
            last = ordered[0]
            for value in ordered[1:]:
                if value - last >= distance:
                    count += 1
                    last = value
            if count >= k:
                best = distance
                low = distance + 1
            else:
                high = distance - 1
        return best
