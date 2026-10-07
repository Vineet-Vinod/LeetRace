class Solution:
    def minDayskVariants(self, points: List[List[int]], k: int) -> int:
        transformed = [(x + y, x - y) for x, y in points]

        def possible(t: int) -> bool:
            # Integral original centers require transformed coordinates of equal parity.
            for center_u in {
                u - t + offset for u, _ in transformed for offset in (0, 1)
            }:
                values = sorted(v for u, v in transformed if abs(u - center_u) <= t)
                for i in range(k - 1, len(values)):
                    low, high = values[i] - t, values[i - k + 1] + t
                    if low <= high and low + ((center_u - low) % 2) <= high:
                        return True
            return False

        low, high = 0, 100
        while low < high:
            middle = (low + high) // 2
            if possible(middle):
                high = middle
            else:
                low = middle + 1
        return low
