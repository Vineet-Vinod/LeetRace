class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        baseline = sum(
            count for count, is_grumpy in zip(customers, grumpy) if not is_grumpy
        )
        recoverable = sum(customers[index] for index in range(minutes) if grumpy[index])
        best = recoverable
        for right in range(minutes, len(customers)):
            if grumpy[right]:
                recoverable += customers[right]
            if grumpy[right - minutes]:
                recoverable -= customers[right - minutes]
            best = max(best, recoverable)
        return baseline + best
