class Solution:
    def maximizeSweetness(self, sweetness: list[int], k: int) -> int:
        low, high = 1, sum(sweetness) // (k + 1)
        while low < high:
            middle = (low + high + 1) // 2
            total = pieces = 0
            for value in sweetness:
                total += value
                if total >= middle:
                    pieces += 1
                    total = 0
            if pieces >= k + 1:
                low = middle
            else:
                high = middle - 1
        return low
