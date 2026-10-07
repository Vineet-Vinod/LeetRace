from bisect import bisect_right
from typing import List


class Solution:
    def minimumRelativeLosses(
        self, prices: List[int], queries: List[List[int]]
    ) -> List[int]:
        p = sorted(prices)
        n = len(p)
        prefix = [0]
        for price in p:
            prefix.append(prefix[-1] + price)
        answer = []
        for k, m in queries:
            affordable = bisect_right(p, k)
            lo, hi = max(0, m - (n - affordable)), min(m, affordable)
            # Choose a prefix below k and a suffix above k; the marginal cost increases.
            while lo < hi:
                mid = (lo + hi) // 2
                expensive_index = n - m + mid
                if p[mid] < 2 * k - p[expensive_index]:
                    lo = mid + 1
                else:
                    hi = mid
            cheap = lo
            expensive = m - cheap
            answer.append(
                prefix[cheap] + 2 * k * expensive - (prefix[n] - prefix[n - expensive])
            )
        return answer
