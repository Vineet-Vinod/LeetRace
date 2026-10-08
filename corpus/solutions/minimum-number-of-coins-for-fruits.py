class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        size = 1
        while size < n + 2:
            size *= 2
        tree = [10**30] * (2 * size)

        def update(index: int, value: int) -> None:
            position = index + size
            tree[position] = value
            position //= 2
            while position:
                tree[position] = min(tree[2 * position], tree[2 * position + 1])
                position //= 2

        def query(left: int, right: int) -> int:
            left += size
            right += size
            result = 10**30
            while left < right:
                if left & 1:
                    result = min(result, tree[left])
                    left += 1
                if right & 1:
                    right -= 1
                    result = min(result, tree[right])
                left //= 2
                right //= 2
            return result

        update(n + 1, 0)
        for fruit in range(n, 0, -1):
            end = min(n + 1, 2 * fruit + 1)
            update(fruit, prices[fruit - 1] + query(fruit + 1, end + 1))
        return query(1, 2)
