class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        count = 0
        value = 0
        for digit in s:
            value = value * 10 + int(digit)
            if value > k:
                value = int(digit)
                count += 1
                if value > k:
                    return -1
        return count + 1
