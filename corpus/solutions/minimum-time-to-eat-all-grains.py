class Solution:
    def minimumTime(self, hens: list[int], grains: list[int]) -> int:
        hens, grains = sorted(hens), sorted(grains)

        def feasible(time: int) -> bool:
            j = 0
            for hen in hens:
                if j == len(grains):
                    return True
                first = grains[j]
                if first < hen:
                    left = hen - first
                    if left > time:
                        return False
                    right = hen + max(time - 2 * left, (time - left) // 2)
                else:
                    right = hen + time
                while j < len(grains) and grains[j] <= right:
                    j += 1
            return j == len(grains)

        low, high = 0, 2 * (max(max(hens), max(grains)) - min(min(hens), min(grains)))
        while low < high:
            mid = (low + high) // 2
            if feasible(mid):
                high = mid
            else:
                low = mid + 1
        return low
