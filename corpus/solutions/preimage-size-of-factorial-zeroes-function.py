class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def first(target):
            low, high = 0, 5 * (target + 1)
            while low < high:
                middle = (low + high) // 2
                value, zeroes = middle, 0
                while value:
                    value //= 5
                    zeroes += value
                if zeroes < target:
                    low = middle + 1
                else:
                    high = middle
            return low

        return first(k + 1) - first(k)
