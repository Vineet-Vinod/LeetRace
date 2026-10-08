class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counts = Counter(nums)
        best = 1
        for value in counts:
            if value == 1:
                count = counts[value]
                best = max(best, count if count % 2 else count - 1)
                continue
            levels = 0
            current = value
            while counts[current] >= 2:
                levels += 1
                current *= current
                if counts[current] >= 1:
                    best = max(best, 2 * levels + 1)
                if current > 10**9:
                    break
        return best
