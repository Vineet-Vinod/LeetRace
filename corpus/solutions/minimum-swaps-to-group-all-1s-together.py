class Solution:
    def minSwaps(self, data: List[int]) -> int:
        window = sum(data)
        if window <= 1:
            return 0
        zeros = sum(value == 0 for value in data[:window])
        best = zeros
        for right in range(window, len(data)):
            zeros -= data[right - window] == 0
            zeros += data[right] == 0
            best = min(best, zeros)
        return best
