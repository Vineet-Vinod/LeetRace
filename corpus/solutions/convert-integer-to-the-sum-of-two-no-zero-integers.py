class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for first in range(1, n):
            second = n - first
            if "0" not in str(first) and "0" not in str(second):
                return [first, second]
        raise ValueError("No valid decomposition")
