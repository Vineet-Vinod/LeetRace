from collections import deque


class Solution:
    def maxHammingDistances(self, nums: list[int], m: int) -> list[int]:
        if len(nums) <= 50:
            return [max((x ^ y).bit_count() for y in nums) for x in nums]
        distance = [-1] * (1 << m)
        queue = deque(set(nums))
        for x in queue:
            distance[x] = 0
        while queue:
            x = queue.popleft()
            for bit in range(m):
                y = x ^ (1 << bit)
                if distance[y] < 0:
                    distance[y] = distance[x] + 1
                    queue.append(y)
        mask = (1 << m) - 1
        return [m - distance[x ^ mask] for x in nums]
