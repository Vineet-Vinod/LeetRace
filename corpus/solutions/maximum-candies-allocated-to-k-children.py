class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low, high = 0, max(candies)
        while low < high:
            size = (low + high + 1) // 2
            if sum(pile // size for pile in candies) >= k:
                low = size
            else:
                high = size - 1
        return low
