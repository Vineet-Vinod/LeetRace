from bisect import bisect_left


class Solution:
    def maximumBeauty(
        self, flowers: list[int], newFlowers: int, target: int, full: int, partial: int
    ) -> int:
        n = len(flowers)
        a = sorted(x for x in flowers if x < target)
        m = len(a)
        if not m:
            return n * full
        prefix = [0]
        for x in a:
            prefix.append(prefix[-1] + x)
        answer = 0
        budget = newFlowers
        for incomplete in range(m, -1, -1):
            if budget < 0:
                break
            minimum = 0
            if incomplete:
                lo, hi = a[0], target - 1
                while lo < hi:
                    mid = (lo + hi + 1) // 2
                    j = bisect_left(a, mid, 0, incomplete)
                    needed = mid * j - prefix[j]
                    if needed <= budget:
                        lo = mid
                    else:
                        hi = mid - 1
                minimum = lo
            answer = max(answer, (n - incomplete) * full + minimum * partial)
            if incomplete:
                budget -= target - a[incomplete - 1]
        return answer
