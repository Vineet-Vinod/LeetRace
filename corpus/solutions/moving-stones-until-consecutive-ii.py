class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        left = 0
        minimum = n
        for right in range(n):
            while stones[right] - stones[left] + 1 > n:
                left += 1
            count = right - left + 1
            if count == n - 1 and stones[right] - stones[left] + 1 == n - 1:
                minimum = min(minimum, 2)
            else:
                minimum = min(minimum, n - count)
        maximum = max(stones[-1] - stones[1] - n + 2, stones[-2] - stones[0] - n + 2)
        return [minimum, maximum]
