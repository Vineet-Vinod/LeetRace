class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibs = [1, 1]
        while fibs[-1] < k:
            fibs.append(fibs[-1] + fibs[-2])
        count = 0
        for value in reversed(fibs):
            if value <= k:
                k -= value
                count += 1
            if k == 0:
                return count
        return count
