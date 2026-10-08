from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        values = sorted(set(nums))
        ranks = {v: i + 1 for i, v in enumerate(values)}
        bit = [0] * (len(values) + 1)

        def update(value, delta):
            i = ranks[value]
            while i < len(bit):
                bit[i] += delta
                i += i & -i

        def select(order):
            i = 0
            step = 1 << len(values).bit_length()
            while step:
                j = i + step
                if j < len(bit) and bit[j] < order:
                    i = j
                    order -= bit[j]
                step >>= 1
            return values[i]

        answer = []
        for i, value in enumerate(nums):
            update(value, 1)
            if i >= k:
                update(nums[i - k], -1)
            if i >= k - 1:
                answer.append((select((k + 1) // 2) + select(k // 2 + 1)) / 2)
        return answer
