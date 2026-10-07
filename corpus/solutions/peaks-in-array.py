from typing import List


class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = [0] * (n + 1)

        def peak(i):
            return int(
                0 < i < n - 1 and nums[i] > nums[i - 1] and nums[i] > nums[i + 1]
            )

        def update(i, delta):
            i += 1
            while i <= n:
                tree[i] += delta
                i += i & -i

        def prefix(i):
            total = 0
            while i:
                total += tree[i]
                i -= i & -i
            return total

        flags = [peak(i) for i in range(n)]
        for i, v in enumerate(flags):
            if v:
                update(i, v)
        answer = []
        for kind, a, b in queries:
            if kind == 1:
                answer.append(prefix(b) - prefix(a + 1) if b > a + 1 else 0)
            else:
                nums[a] = b
                for i in range(max(0, a - 1), min(n, a + 2)):
                    value = peak(i)
                    update(i, value - flags[i])
                    flags[i] = value
        return answer
